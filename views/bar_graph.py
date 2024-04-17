'''
CS5001 Spring 2024 Final Project
@WeifanLi

function that used to display bar graph based on Geo Area
'''
import plotly.express as px

'''
    Purpose: Display a bar graph representing the number of food vendors in each geographical area using Plotly.

    Parameters:
        counts (Series): A pandas Series with geographical areas as the index and the number of food vendors as the values.

    Returns: None. This function directly displays the bar graph and does not return any value.

    Raises:
        None
    '''


def show_food_vendor_bar_graph(counts):
    fig = px.bar(counts, x=counts.index, y=counts.values, labels={'x': 'Geographical Area', 'y': 'Number of Food Vendors'},
                 title='Number of Food Vendors by Geographical Area')
    fig.show()
