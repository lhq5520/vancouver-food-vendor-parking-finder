'''
VanStreet Parking       
@WeifanLi

fetch online Json data function
'''
import requests


def fetch_raw_data(url):
    '''
    Fetch parking data from the given URL and return cleaned and structured data.
    '''
    # Sending a GET request to the URL
    response = requests.get(url)
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.text  # get raw data(String)
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
