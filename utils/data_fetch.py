'''
CS5001 Spring 2024 Final Project
@WeifanLi

get all spcified data for car parking from parking_meter

format data from regular expression to tailored class
'''

import requests
import re
from models.Car_Parking import CarParking
from models.Food_Vendor import FoodVendor
from data_dashboard import CARPARKING_URL, FOOD_VENDOR_URL


def fetch_raw_data(url):
    '''
    Purpose: Fetch raw data from the specified URL by sending a GET request. 
    It raises an HTTPError if the request fails or returns a non-200 status code.

    Parameters:
        url (str): The URL from which to fetch data.

    Returns:
        data (str): The raw text data retrieved from the URL if the request is successful.

    Raises:
        HTTPError: If the HTTP request did not succeed.
    '''

    # Sending a GET request to the URL
    response = requests.get(url)
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.text  # get raw data(String)
        return data
    else:
        raise requests.HTTPError(f"Failed to fetch data, HTTP status: {response.status_code}")


# -----------------car_parking_fetch--------------------
# fetch car data
def get_all_meterhead() -> str:
    '''
    Purpose: Extract all meterhead descriptions from parking meter data. 
    Raises a ValueError if no meterheads are found.

    Parameters:
        no parameters

    Returns:
        meterheads (list): A list of all meterhead descriptions extracted from the data.

    Raises:
        ValueError: If no meterhead entries are found in the data.
    '''
    raw_data = fetch_raw_data(CARPARKING_URL)
    meterhead_regex = r'"meterhead":\s*.([^"]*).'  # Regex to find meter IDs
    meterheads = re.findall(meterhead_regex, raw_data)  # Find all matches
    if not meterheads:
        raise ValueError("No meterheads found in the data.")
    return meterheads


def get_all_meter_id() -> str:
    '''
    Purpose: Retrieve all meter IDs from the parking meter data using a regex pattern. Raises a ValueError if no meter IDs are found.

    Parameters:
        no parameters

    Returns:
        meter_ids (list): A list of all meter IDs found in the data.

    Raises:
        ValueError: If no meter IDs are found in the data.
    '''
    raw_data = fetch_raw_data(CARPARKING_URL)
    meter_id_regex = r'"meterid": "(\w+)"'  # Regex to find meter IDs
    meter_ids = re.findall(meter_id_regex, raw_data)  # Find all matches
    if not meter_ids:
        raise ValueError("No meter IDs found in the data.")
    return meter_ids


def get_all_coordinates() -> tuple:
    '''
    Purpose: Extract and convert geographic coordinates for parking meters from the raw data. It raises a ValueError if no coordinates are found or if there is an error during conversion.

    Parameters:
        no parameters

    Returns:
        coordinates_floats (list of tuples): A list of tuples containing the longitude and latitude as float values.

    Raises:
        ValueError: If no coordinates are found or there is an error during the float conversion.
    '''
    # fetch part
    raw_data = fetch_raw_data(CARPARKING_URL)
    coordinate_regex = r'"coordinates":\s\[(.\d\w*.\d*,\s\d*.\d*)\]'  # Regex to find coordinate
    coordinates = re.findall(coordinate_regex, raw_data)  # Find all matches
    if not coordinates:
        raise ValueError("No coordinates found in the data.")

    # format part
    coordinates_floats = []
    for coord_str in coordinates:
        lon_str, lat_str = coord_str.split(',')
        lon, lat = float(lon_str), float(lat_str)
        coordinates_floats.append((lon, lat))
    return coordinates_floats


def get_all_pay_phone_id() -> str:
    '''
    Purpose: Retrieve all PayByPhone IDs from the parking meter data using a regex pattern. Raises a ValueError if no PayByPhone IDs are found.

    Parameters:
        no parameters

    Returns:
        pay_phones (list): A list of all PayByPhone IDs found in the data.

    Raises:
        ValueError: If no PayByPhone IDs are found in the data.
    '''
    raw_data = fetch_raw_data(CARPARKING_URL)
    pay_phone_regex = r'"pay_phone":\s*.(\w*).'  
    pay_phones = re.findall(pay_phone_regex, raw_data)  # Find all matches
    if not pay_phones:
        raise ValueError("No paybyphone ID found in the data.")
    return pay_phones


def get_all_creditcard_support_status() -> str:
    '''
    Purpose: Extract credit card support statuses from parking meter data.
    Raises a ValueError if no statuses are found.

    Parameters:
        no parameters

    Returns:
        creditcard_support_status (list): A list indicating
        whether credit card support is available at the meters.

    Raises:
        ValueError: If no credit card support statuses are found.
    '''
    raw_data = fetch_raw_data(CARPARKING_URL)
    creditcard_support_status_regex = r'"creditcard":\s*.(\w*).'  
    creditcard_support_status = re.findall(creditcard_support_status_regex, raw_data)  # Find all matches
    if not creditcard_support_status:
        raise ValueError("No creditcard_support status found in the data.")
    return creditcard_support_status


def get_all_geo_local_area() -> str:
    '''
    Purpose: Extract geographical local areas from parking meter data using
    a regex pattern. Raises a ValueError if no areas are found.

    Parameters:
        no parameters

    Returns:
        geo_local_area (list): A list of geographical local areas as found
        in the data.

    Raises:
        ValueError: If no geographical local areas are found in the data.
    '''
    raw_data = fetch_raw_data(CARPARKING_URL)
    geo_local_area_regex = r'"geo_local_area":\s*"([^"]*)"'
    geo_local_area = re.findall(geo_local_area_regex, raw_data)  # Find all matches
    if not geo_local_area:
        raise ValueError("No geo local area found in the data.")
    return geo_local_area


def get_all_timeineffee() -> str:
    '''
    Purpose: Retrieve information about the time meters are in effect 
    from parking meter data. Raises a ValueError if no such information is found.

    Parameters:
        no parameters

    Returns:
        timeineffe (list): A list of strings describing the times when meters 
        are in effect.

    Raises:
        ValueError: If no time in effect information is found.
    '''
    raw_data = fetch_raw_data(CARPARKING_URL)
    timeineffe_regex = r'"timeineffe":\s.([^"]*).'
    # timeineffe_regex = r'"timeineffe":\s*(?:"METER IN EFFECT:\s*(\d{1,2}:\d{2} [AP]M TO \d{1,2}:\d{2} [AP]M)"|null)'
    timeineffe = re.findall(timeineffe_regex, raw_data)  # Find all matches
    if not timeineffe:
        raise ValueError("No time in effect information found in the data.")
    return timeineffe


# -----------------food_vendor_fetch--------------------
def get_all_key() -> str:
    '''
    Purpose: Retrieve all unique keys from the food vendor data 
    using a regex pattern. Raises a ValueError if no keys are found.

    Parameters:
        no parameters

    Returns:
        key (list): A list of keys found in the data.

    Raises:
        ValueError: If no keys are found in the data.
    '''
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    key_regex = r'"key":\s*\W(null|[^"]*)'
    key = re.findall(key_regex, raw_data)
    if not key:
        raise ValueError("No keys found in the data.")
    return key


def get_all_businessname() -> str:
    '''
    Purpose: Extract all business names from the food vendor data.
    This function uses regex to parse the raw data fetched from a URL.
    It raises a ValueError if no business names are found.

    Parameters:
        no parameters

    Returns:
        businessnames (list): A list of business names found in the data.

    Raises:
        ValueError: If no business names are found in the data.
    '''
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    businessname_regex = r'"business_name":\s*\W(null|[^"]*)'
    businessnames = re.findall(businessname_regex, raw_data)
    if not businessnames:
        raise ValueError("No business names found in the data.")
    return businessnames


def get_all_description() -> str:
    '''
    Purpose: Fetch descriptions of food vendors from the raw data
    using a regular expression. Raises a ValueError if no descriptions are found.

    Parameters:
        no parameters

    Returns:
        descriptions (list): A list of descriptions
        for each food vendor found in the data.

    Raises:
        ValueError: If no descriptions are found in the data.
    '''
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    description_regex = r'"description":\s*\W(null|[^"]*)'
    descriptions = re.findall(description_regex, raw_data)
    if not descriptions:
        raise ValueError("No descriptions found in the data.")
    return descriptions


def get_all_food_vendor_geo_local_area() -> str:
    '''
    Purpose: Extract geographical local areas from the food vendor data 
    using a regex pattern. Raises a ValueError if no geographical areas are found.

    Parameters:
        no parameters

    Returns:
        geo_local_area (list): A list of geographical local areas found in the data.

    Raises:
        ValueError: If no geographical local areas are found in the data.
    '''
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    geo_local_area_regex = r'"geo_localarea":\s*"([^"]*)"'
    geo_local_area = re.findall(geo_local_area_regex, raw_data)  # Find all matches
    if not geo_local_area:
        raise ValueError("No geographical local areas found in the data.")
    return geo_local_area


def get_all_food_vendor_coordinates() -> tuple:
    '''
    Purpose: Extract and convert geographic coordinates from the food vendor data. 
    This function parses coordinate strings, splits them, 
    and converts them to float values. Raises a ValueError 
    if no coordinates are found or if there is an error during conversion.

    Parameters:
        no parameters

    Returns:
        coordinates_floats (list of tuples): A list of tuples, each containing the longitude and latitude as float values.

    Raises:
        ValueError: If no coordinates are found or there is an error during the float conversion.
    '''
    # fetch part
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    coordinate_regex = r'"coordinates":\s\[(.\d\w*.\d*,\s\d*.\d*)\]'  # Regex to find coordinate
    coordinates = re.findall(coordinate_regex, raw_data)  # Find all matches
    if not coordinates:
        raise ValueError("No coordinates found in the data.")

    # convert coordinates into list of tuples
    coordinates_floats = []
    for coord_str in coordinates:
        lon_str, lat_str = coord_str.split(',')
        lon, lat = float(lon_str), float(lat_str)
        coordinates_floats.append((lon, lat))
    return coordinates_floats
