# Vancouver Food Vendor → Nearest Parking Finder (GIS)

This project is a GUI-based data dashboard for exploring van/vehicle parking and food vendor information in Vancouver. It fetches data, processes it with Python, and visualises it with interactive charts and a parking map.

## Environment

- Recommended Python version: **3.12.3** (the project was developed and tested with this version).

## Installation

1. (Optional but recommended) Create and activate a virtual environment in the project root:

   ```powershell
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

2. Install dependencies from `requirements.txt`:

   ```powershell
   pip install -r requirements.txt
   ```

   Main packages include:

   - `plotly==5.20.0`
   - `pandas`
   - `requests`

## How to Run

1. Make sure you are in the project root folder `Van_Parking_Info_System`.
2. Activate your virtual environment (if you created one).
3. Run the main dashboard script:

   ```powershell
   python data_dashboard.py
   ```

4. Follow the GUI instructions:
   - Load or refresh parking data.
   - View bar graphs and other visualisations.
   - Explore the parking map and related information panels.

## Project Structure

- `data_dashboard.py`: Entry point of the application, launching the GUI dashboard.
- `models/`: Data models for parking spots, vehicles, food vendors, etc.
- `utils/`: Utility functions for data fetching and processing (e.g. API/file access).
- `views/`: GUI components, bar charts, parking map, and other visual elements.
- `tests/`: Unit tests to verify models and utilities.

## Tips

- If you see "ModuleNotFoundError" or similar, make sure you have installed all dependencies in the active environment with `pip install -r requirements.txt`.
- After changing the code, re-run `python data_dashboard.py` to refresh the GUI.
 - To display the interactive parking map, you must provide **your own Mapbox access token** in the `.mapbox_token` file in the project root (one token string per file, do **not** commit your personal token to Git).

## Screenshots

Main GUI window:

![Main GUI window](images/gui_main_menu.png)

Search food vendors by type:

![Search food vendors by type](images/gui_food_vendor_type.png)

Look up parking info by geo area:

![Look up parking info by geo area](images/gui_geo_area_parking.png)

Look up food vendors by geo area and unique key:

![Look up food vendor by geo area](images/gui_geo_area_vendor.png)
![Look up food vendor by unique key](images/gui_vendor_unique_key.png)

Nearest parking spot on interactive map:

![Nearest parking spot on map](images/map_nearest_parking.png)

Number of food vendors by geographical area (sample and full data):

![Food vendors by area (sample)](images/bar_food_vendors_small.png)
![Food vendors by area (full data)](images/bar_food_vendors_full.png)
