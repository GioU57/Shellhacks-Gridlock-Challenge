import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) in miles.
    """
    if pd.isna(lat1) or pd.isna(lon1) or pd.isna(lat2) or pd.isna(lon2):
        return np.nan
    
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 3956.0  # Radius of earth in miles
    return c * r

def get_projects_data():
    """
    Returns pandas DataFrame of all planned utility transmission projects from 
    Dominion Energy South Carolina (DESC) and Georgia Power (GPC) grounded in notebook data.
    """
    projects = [
        {
            "project_id": "DESC_1",
            "utility": "Dominion Energy South Carolina",
            "utility_short": "DESC",
            "state": "SC",
            "project_name": "Stevens Creek - Hooks 115 kV / LR Plumb Branch 46 kV Rebuilds",
            "name_a": "Stevens Creek Substation",
            "lat_a": 33.562599,
            "lon_a": -82.051362,
            "name_b": "Hooks Substation",
            "lat_b": 33.660127,
            "lon_b": -82.195931,
            "lat_center": 33.562599,
            "lon_center": -82.051362,
            "in_service_date": "2024-12-31",
            "voltage_kv": "115 / 46 kV",
            "project_type": "Line Rebuild",
            "description": "9.5 miles line rebuild in corridor SPDC to replace aging structures and address end-of-life reliability issues.",
            "est_cost_usd": 11745543
        },
        {
            "project_id": "DESC_2",
            "utility": "Dominion Energy South Carolina",
            "utility_short": "DESC",
            "state": "SC",
            "project_name": "Hooks - Thurmond 115 kV Tie: Rebuild",
            "name_a": "Hooks Substation",
            "lat_a": 33.562599,
            "lon_a": -82.051362,
            "name_b": "Thurmond Substation",
            "lat_b": 33.660127,
            "lon_b": -82.195931,
            "lat_center": 33.660127,
            "lon_center": -82.195931,
            "in_service_date": "2024-12-31",
            "voltage_kv": "115 kV",
            "project_type": "Tie Rebuild",
            "description": "Rebuild 2.3 miles of line between Hooks and Thurmond on existing R/W using steel poles and 1272 ACSR conductor.",
            "est_cost_usd": 2200080
        },
        {
            "project_id": "DESC_3",
            "utility": "Dominion Energy South Carolina",
            "utility_short": "DESC",
            "state": "SC",
            "project_name": "Jasper - Okatie 230 kV #2: Construct",
            "name_a": "Jasper Substation",
            "lat_a": 32.359120,
            "lon_a": -81.124600,
            "name_b": "Okatie Substation",
            "lat_b": 32.333758,
            "lon_b": -81.032495,
            "lat_center": 32.346439,
            "lon_center": -81.078548,
            "in_service_date": "2025-12-31",
            "voltage_kv": "230 kV",
            "project_type": "New Line / Substation Expansion",
            "description": "Expand Okatie sub, add 230-115 autobank and fold Jasper - Yemassee 230 kV line. Addresses load growth and NERC TPL criteria.",
            "est_cost_usd": 11116933
        },
        {
            "project_id": "DESC_4",
            "utility": "Dominion Energy South Carolina",
            "utility_short": "DESC",
            "state": "SC",
            "project_name": "Queensboro - Ft Johnson 115 kV & Queensboro-Bayfront 115 kV",
            "name_a": "Queensboro Substation",
            "lat_a": 32.722793,
            "lon_a": -79.967332,
            "name_b": "Ft Johnson Substation",
            "lat_b": 32.750000,
            "lon_b": -79.930000,
            "lat_center": 32.722793,
            "lon_center": -79.967332,
            "in_service_date": "2023-12-31",
            "voltage_kv": "115 kV",
            "project_type": "Line Replacement",
            "description": "Replace line and aging structures that have reached end of life in James Island section.",
            "est_cost_usd": 5300000
        },
        {
            "project_id": "DESC_5",
            "utility": "Dominion Energy South Carolina",
            "utility_short": "DESC",
            "state": "SC",
            "project_name": "Okatie - Bluffton 115 kV: Rebuild",
            "name_a": "Okatie Substation",
            "lat_a": 32.333758,
            "lon_a": -81.032495,
            "name_b": "Bluffton Substation",
            "lat_b": 32.235027,
            "lon_b": -80.853384,
            "lat_center": 32.284393,
            "lon_center": -80.942940,
            "in_service_date": "2025-06-01",
            "voltage_kv": "115 kV",
            "project_type": "Line Rebuild",
            "description": "Rebuild 115 kV line corridor connecting Okatie and Bluffton substations for grid hardening and load growth.",
            "est_cost_usd": 8750000
        },
        {
            "project_id": "GPC_1",
            "utility": "Georgia Power",
            "utility_short": "GPC",
            "state": "GA",
            "project_name": "EVANS PRIMARY - THURMOND DAM (USA) #5 115KV REBUILD",
            "name_a": "Evans Primary Substation",
            "lat_a": 33.543994,
            "lon_a": -82.168648,
            "name_b": "Thurmond Dam #5 Substation",
            "lat_b": 33.660127,
            "lon_b": -82.195931,
            "lat_center": 33.602061,
            "lon_center": -82.182290,
            "in_service_date": "2033-06-01",
            "voltage_kv": "115 kV",
            "project_type": "Line Rebuild",
            "description": "Rebuild 8.9 miles of 115 kV line with 1351 ACSS Martin conductor and upgrade main bus at Thurmond Dam.",
            "est_cost_usd": 15200000
        },
        {
            "project_id": "GPC_2",
            "utility": "Georgia Power",
            "utility_short": "GPC",
            "state": "GA",
            "project_name": "SAV: MCINTOSH - PURRYSBURG 230KV REACTORS",
            "name_a": "McIntosh Substation",
            "lat_a": 32.352116,
            "lon_a": -81.175112,
            "name_b": "Purrysburg Substation",
            "lat_b": 32.360000,
            "lon_b": -81.110000,
            "lat_center": 32.352116,
            "lon_center": -81.175112,
            "in_service_date": "2026-06-01",
            "voltage_kv": "230 kV",
            "project_type": "Reactor Installation",
            "description": "Install 230 kV series reactors on the McIntosh - Purrysburg cross-border tie line for power flow control.",
            "est_cost_usd": 6800000
        },
        {
            "project_id": "GPC_3",
            "utility": "Georgia Power",
            "utility_short": "GPC",
            "state": "GA",
            "project_name": "SAV: GOSHEN (SAV) - MCINTOSH 115KV LINE REBUILD",
            "name_a": "Goshen Substation",
            "lat_a": 32.248701,
            "lon_a": -81.209472,
            "name_b": "McIntosh Substation",
            "lat_b": 32.352116,
            "lon_b": -81.182105,
            "lat_center": 32.300409,
            "lon_center": -81.195789,
            "in_service_date": "2027-06-01",
            "voltage_kv": "115 kV",
            "project_type": "Line Rebuild",
            "description": "Rebuild 6.7 miles section of 115 kV line using 795 ACSR Drake conductor in Savannah border region.",
            "est_cost_usd": 9400000
        },
        {
            "project_id": "GPC_4",
            "utility": "Georgia Power",
            "utility_short": "GPC",
            "state": "GA",
            "project_name": "MITCHELL - NORTH TIFTON 230KV RECONDUCTOR",
            "name_a": "Mitchell Substation",
            "lat_a": 31.447121,
            "lon_a": -84.133843,
            "name_b": "North Tifton Substation",
            "lat_b": 31.478089,
            "lon_b": -83.549130,
            "lat_center": 31.462605,
            "lon_center": -83.841487,
            "in_service_date": "2025-05-01",
            "voltage_kv": "230 kV",
            "project_type": "Reconductoring",
            "description": "Reconductor 230 kV line between Mitchell and North Tifton to increase thermal transmission capacity.",
            "est_cost_usd": 12500000
        },
        {
            "project_id": "GPC_5",
            "utility": "Georgia Power",
            "utility_short": "GPC",
            "state": "GA",
            "project_name": "JESUP - LUDOWICI PRIMARY 115KV REBUILD",
            "name_a": "Jesup Substation",
            "lat_a": 31.603106,
            "lon_a": -81.924947,
            "name_b": "Ludowici Primary Substation",
            "lat_b": 31.721597,
            "lon_b": -81.743703,
            "lat_center": 31.662352,
            "lon_center": -81.834325,
            "in_service_date": "2025-06-01",
            "voltage_kv": "115 kV",
            "project_type": "Line Rebuild",
            "description": "Rebuild 115 kV line section between Jesup and Ludowici to support regional load growth.",
            "est_cost_usd": 8100000
        }
    ]
    df = pd.DataFrame(projects)
    df["in_service_date"] = pd.to_datetime(df["in_service_date"])
    return df

def calculate_overlaps(df_projects, max_distance_mi=25.0, max_time_gap_years=10.0):
    """
    Computes cross-utility project pairs within distance and time thresholds.
    """
    desc_df = df_projects[df_projects["utility_short"] == "DESC"].copy()
    gpc_df = df_projects[df_projects["utility_short"] == "GPC"].copy()
    
    overlaps = []
    overlap_idx = 1
    
    for _, desc_row in desc_df.iterrows():
        for _, gpc_row in gpc_df.iterrows():
            dist = haversine_distance(
                desc_row["lat_center"], desc_row["lon_center"],
                gpc_row["lat_center"], gpc_row["lon_center"]
            )
            
            time_gap_days = abs((desc_row["in_service_date"] - gpc_row["in_service_date"]).days)
            time_gap_years = time_gap_days / 365.25
            
            if dist <= max_distance_mi and time_gap_years <= max_time_gap_years:
                # Composite priority score (0-100)
                # Distance score: closer = higher score
                dist_score = max(0, (1 - (dist / 25.0))) * 60
                # Temporal score: closer in time = higher score
                time_score = max(0, (1 - (time_gap_years / 10.0))) * 40
                composite_score = round(dist_score + time_score, 1)
                
                # Estimated combined cost & potential savings (10-25% from co-location / shared ROW)
                total_combined_cost = desc_row["est_cost_usd"] + gpc_row["est_cost_usd"]
                est_savings_usd = round(total_combined_cost * (0.15 * (1 - dist/50.0)), -3)
                
                overlaps.append({
                    "overlap_id": f"OVL_{overlap_idx}",
                    "distance_mi": round(dist, 2),
                    "time_gap_days": time_gap_days,
                    "time_gap_years": round(time_gap_years, 1),
                    "composite_score": composite_score,
                    "utility_a": desc_row["utility"],
                    "project_id_a": desc_row["project_id"],
                    "project_name_a": desc_row["project_name"],
                    "in_service_a": desc_row["in_service_date"].strftime("%Y-%m-%d"),
                    "voltage_a": desc_row["voltage_kv"],
                    "lat_a": desc_row["lat_center"],
                    "lon_a": desc_row["lon_center"],
                    "utility_b": gpc_row["utility"],
                    "project_id_b": gpc_row["project_id"],
                    "project_name_b": gpc_row["project_name"],
                    "in_service_b": gpc_row["in_service_date"].strftime("%Y-%m-%d"),
                    "voltage_b": gpc_row["voltage_kv"],
                    "lat_b": gpc_row["lat_center"],
                    "lon_b": gpc_row["lon_center"],
                    "est_savings_usd": est_savings_usd,
                    "border_region": "Savannah River / Augusta-Evans" if desc_row["lat_center"] > 33 else "Savannah River / Coastal-Purrysburg"
                })
                overlap_idx += 1
                
    overlaps_df = pd.DataFrame(overlaps)
    if not overlaps_df.empty:
        overlaps_df = overlaps_df.sort_values(by="composite_score", ascending=False).reset_index(drop=True)
    return overlaps_df

if __name__ == "__main__":
    df_p = get_projects_data()
    print(f"Loaded {len(df_p)} total projects.")
    df_o = calculate_overlaps(df_p)
    print(f"Calculated {len(df_o)} cross-utility overlaps:")
    print(df_o[["overlap_id", "distance_mi", "time_gap_days", "composite_score", "project_name_a", "project_name_b"]])
