'''
CS5001 Spring 2024 Final Project
@WeifanLi

map function that used to display map
'''
import plotly.express as px


def display_parking_spot_map(data_frame):
    """
    Purpose: Display a map visualization of parking spots using data from a DataFrame.
             The function configures Plotly to use Mapbox for geographic plotting, visualizing
             parking locations with longitude, latitude, and additional data on meterhead.

    Parameters:
        data_frame (pd.DataFrame): A pandas DataFrame containing at least the columns 'lon' (longitude),
                                   'lat' (latitude), and 'meterhead', where 'meterhead' might be used
                                   to represent different types of parking meters or statuses.

    Returns: None. Displays a map visualization in a web browser using Plotly's interactive capabilities.

    Raises:
        FileNotFoundError: If the '.mapbox_token' file cannot be found, indicating that the Mapbox
                           access token necessary for plotting geographic data is missing.
    """
    try:
        px.set_mapbox_access_token(open(".mapbox_token").read())
    except FileNotFoundError:
        raise FileNotFoundError("The Mapbox access token file '.mapbox_token' is not found.")

    df = data_frame
    fig = px.scatter_mapbox(df,
                        lon="lon",
                        lat="lat",
                        color="meterhead",
                        text='meterhead',
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=15,
                        )
    fig.update_layout(title="The nearest parking based on your food vendor search", legend_title="Type of Parking")
    fig.show()
