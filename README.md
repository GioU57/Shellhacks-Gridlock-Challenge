<<<<<<< HEAD
<<<<<<< HEAD
# Shellhacks-Gridlock-Challenge
=======
=======
>>>>>>> 0820ac1d4267c350c3620cfa17c0a889b6bc78fb
# Gridlock: Bridging the Utility Infrastructure Coordination Gap

A Streamlit web application that identifies geographic and temporal overlaps between planned transmission construction projects of neighboring electric utilities, specifically **Dominion Energy South Carolina (DESC)** and **Georgia Power (GPC)**.

Historically, utilities have planned in isolation, leading to duplicated and inefficient work. By flagging projects that are physically close and scheduled in the same build window, this tool highlights opportunities to share resources (like construction crews and right-of-way), directly aligning with the regional coordination goals of **FERC Order No. 1920**.

## Key Features

* **Interactive Spatial Map**: Visualizes transmission lines and substations using Folium. It provides an interactive UI showing both utilities' planned projects, allowing users to pan, zoom, and click into locations, while visually highlighting where overlaps occur based on a $\le$ 25-mile threshold.


* **Ranked Coordination Matrix**: Provides a ranked list of the top coordination opportunities, sorting cross-utility project pairs by a composite priority score. It treats geographic proximity as the primary signal and the time gap in days as a strong secondary signal.


* **Bonus - Cost & Impact Analysis (OVL_2)**: Includes an interactive scenario modeler that estimates capital savings from shared right-of-way between DESC and GPC. It translates the 5.65-mile geographic overlap and 152-day timeline overlap into tangible acreage and equipment mobilization savings.
* **Decoupled Data Architecture**: Separates the raw, publicly sourced utility planning data (such as the Georgia Power Ten Year Transmission Expansion Plan) from the rendering logic for clean, modular updates.



## Project Structure

```text
gridlock_app/
├── app.py              # Main Streamlit web application and dashboard UI
├── requirements.txt    # Required Python packages (Streamlit, Folium, Pandas)
├── run.sh              # Mac/Linux quick-start script
├── run.bat             # Windows quick-start script
└── data/               # Directory containing the public utility data
    ├── projects.csv    # Coordinate and timeline data for DESC and GPC
    └── overlaps.csv    # Pre-calculated haversine distances and timeline gaps

```

## How to Run Locally

You can launch the environment and application automatically using the provided startup scripts.

**For Mac/Linux:**

```bash
chmod +x run.sh
./run.sh

```

**For Windows:**
Double-click `run.bat` or execute it in your command prompt:

```cmd
run.bat

```

*Alternatively, to run it manually:*

1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`

## Deployment to Streamlit Community Cloud

1. Push this repository to GitHub. Ensure your `venv/` folder is listed in your `.gitignore`.
2. Visit [share.streamlit.io](https://share.streamlit.io/?utm_source=gemini).
<<<<<<< HEAD
3. Connect your repository, select `app.py` as the main file, and click **Deploy**!
>>>>>>> 0820ac1 (Initial commit for Gridlock challenge app)
=======
3. Connect your repository, select `app.py` as the main file, and click **Deploy**!
>>>>>>> 0820ac1d4267c350c3620cfa17c0a889b6bc78fb
