import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
from io import StringIO

# 1. Embedded Challenge Data
# Using the provided sample data for Dominion Energy South Carolina (DESC) and Georgia Power (GPC)

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the great circle distance in miles between two points on the earth."""
    r = 3959.87433 # Radius of earth in miles
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi/2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda/2)**2
    return 2 * r * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

@st.cache_data
def load_and_process_data():
    # 1. Load the projects for the map points
    df = pd.read_csv("data/projects.csv")
    df['in_service_date'] = pd.to_datetime(df['in_service_date'])
    
    # 2. Load the pre-calculated overlaps for the table and lines
    overlaps = pd.read_csv("data/overlaps.csv")
    
    # 3. Rename spreadsheet columns to match what the dashboard expects
    overlaps = overlaps.rename(columns={
        'project_name_a': 'project_name_desc',
        'project_name_b': 'project_name_gpc',
        'time_gap (day)': 'time_gap_days'
    })
    
    # Add the ranking column back in
    overlaps['overlap_rank'] = overlaps.index + 1
    
    # 4. Attach Utility A (DESC) coordinates to the overlap rows
    overlaps = overlaps.merge(
        df[['project_id', 'lat_center', 'lon_center']], 
        left_on='project_id_a', right_on='project_id', how='left'
    ).rename(columns={'lat_center': 'lat_center_desc', 'lon_center': 'lon_center_desc'}).drop(columns=['project_id'])
    
    # 5. Attach Utility B (GPC) coordinates to the overlap rows
    overlaps = overlaps.merge(
        df[['project_id', 'lat_center', 'lon_center']], 
        left_on='project_id_b', right_on='project_id', how='left'
    ).rename(columns={'lat_center': 'lat_center_gpc', 'lon_center': 'lon_center_gpc'}).drop(columns=['project_id'])
    
    return df, overlaps

def create_map(projects_df, overlaps_df, center, zoom):
    """Generates an interactive Folium map showing projects and overlapping connections."""
    m = folium.Map(location=center, zoom_start=zoom);
    
    # Plot all projects
    for _, row in projects_df.iterrows():
        color = 'blue' if row['utility'] == 'Dominion Energy South Carolina' else 'red'
        folium.CircleMarker(
            location=[row['lat_center'], row['lon_center']],
            radius=6,
            popup=f"<b>{row['utility']}</b><br>{row['project_name']}<br>Date: {row['in_service_date'].date()}",
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7
        ).add_to(m)
        
    # Draw lines connecting overlapping projects
    for _, row in overlaps_df.iterrows():
        loc_desc = [row['lat_center_desc'], row['lon_center_desc']]
        loc_gpc = [row['lat_center_gpc'], row['lon_center_gpc']]
        folium.PolyLine(
            locations=[loc_desc, loc_gpc],
            color='purple',
            weight=3,
            opacity=0.8,
            dash_array='5, 5',
            tooltip=f"Overlap: {row['distance_mi']:.2f} mi | Gap: {row['time_gap_days']} days"
        ).add_to(m)
        
    return m

# --- Streamlit UI Layout ---
st.set_page_config(layout="wide", page_title="Gridlock Challenge")

st.title("Gridlock: Utility Infrastructure Coordination Tool")
st.markdown("Identifying cross-utility construction overlaps to reduce redundant work and share resources.")

# Load Data
projects, overlaps = load_and_process_data()
# Initialize session state for map coordinates
if 'map_center' not in st.session_state:
    st.session_state.map_center = [32.9, -81.5]
if 'map_zoom' not in st.session_state:
    st.session_state.map_zoom = 7
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Interactive Geographic Overlap Map")
    st.markdown("**Blue**: Dominion Energy | **Red**: Georgia Power | **Purple Dashed**: < 25mi Overlap")
    
    # View toggles for the 5 geographic clusters
    st.markdown("**Jump to Location:**")
    b1, b2, b3, b4, b5, b6 = st.columns(6)
    
    if b1.button("Augusta", help="Cluster: 3 Projects"):
        st.session_state.map_center, st.session_state.map_zoom = [33.60, -82.14], 11
        st.rerun()
    if b2.button("Savannah", help="Cluster: 4 Projects"):
        st.session_state.map_center, st.session_state.map_zoom = [32.31, -81.08], 11
        st.rerun()
    if b3.button("Charleston", help="Standalone: DESC_4"):
        st.session_state.map_center, st.session_state.map_zoom = [32.72, -79.96], 12
        st.rerun()
    if b4.button("Tifton", help="Standalone: GPC_4"):
        st.session_state.map_center, st.session_state.map_zoom = [31.46, -83.84], 12
        st.rerun()
    if b5.button("Jesup", help="Standalone: GPC_5"):
        st.session_state.map_center, st.session_state.map_zoom = [31.66, -81.83], 12
        st.rerun()
    if b6.button("↺ Reset", help="Default View"):
        st.session_state.map_center, st.session_state.map_zoom = [32.9, -81.5], 7
        st.rerun()

    # Pass the session state variables into the map generator
    gridlock_map = create_map(projects, overlaps, st.session_state.map_center, st.session_state.map_zoom)
    
    # Render using the modern st_folium function
    st_folium(gridlock_map, width=700, height=500)

with col2:
    st.subheader("Ranked Coordination Opportunities")
    st.markdown("Top overlaps ranked by geographic proximity, followed by construction timeline proximity.")
    
    display_df = overlaps[[
        'overlap_rank', 'project_name_desc', 'project_name_gpc', 'distance_mi', 'time_gap_days'
    ]].rename(columns={
        'overlap_rank': 'Rank',
        'project_name_desc': 'DESC Project',
        'project_name_gpc': 'GPC Project',
        'distance_mi': 'Distance (mi)',
        'time_gap_days': 'Time Gap (Days)'
    })

    # Format the distance column
    display_df['Distance (mi)'] = display_df['Distance (mi)'].map("{:.2f}".format)
    
    # Use st.table to bypass the Arrow rendering engine completely
    st.table(display_df)

    # --- BONUS POINTS SECTION ---
st.divider()
st.subheader("💡 Bonus Points: Cost & Impact Analysis (OVL_2)")

bonus_col1, bonus_col2 = st.columns([2, 1])

with bonus_col1:
    st.markdown("""
    **The Opportunity: Right-of-Way (ROW) Sharing**
    * **Dominion Energy (DESC_3)**: Jasper - Okatie 230 kV #2 Construct ($18M Budget, 6.5 miles)
    * **Georgia Power (GPC_2)**: SAV: MCINTOSH - PURRYSBURG 230KV REACTORS
    
    **The Impact:**
    These projects are located just **5.65 miles apart** and are scheduled to go into service within **152 days** of each other. 
    
    Rather than acquiring separate strips of land, the utilities can coordinate to reuse existing rights-of-way or clear a single shared corridor. Acquiring new right-of-way is a major schedule bottleneck. By sharing a corridor for this ~5.6 mile stretch, the utilities avoid purchasing and clear-cutting approximately **70 to 100 acres** of redundant land. Because the DESC project has an $18,000,000 total estimated cost, pooling heavy equipment mobilization and land acquisition for this overlapping section could yield millions in direct ratepayer savings.
    """)

with bonus_col2:
    st.info("""
    **Overlap Metrics**
    * **Distance:** 5.65 miles
    * **Time Gap:** 152 days
    * **Coordination Potential:** High
    """)


# Add a GitHub repository link button
st.sidebar.markdown("---")
st.sidebar.link_button("🔗 View Code on GitHub", "https://github.com/GioU57/Shellhacks-Gridlock-Challenge")
