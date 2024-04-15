import plotly.express as px


def display_parking_spot_map(data_frame):
    px.set_mapbox_access_token(open(".mapbox_token").read())
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