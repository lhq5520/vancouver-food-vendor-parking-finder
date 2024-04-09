import re
from utils.raw_data_fetch import fetch_raw_data

URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/food-vendors/exports/json?lang=en&timezone=America%2FLos_Angeles"


def get_all_businessname() -> str:
    raw_data = fetch_raw_data(URL)
    businessname_regex = r'"business_name":\s*\W(null|[^"]*)'  
    businessnames = re.findall(businessname_regex, raw_data)
    return businessnames


def get_all_description() -> str:
    raw_data = fetch_raw_data(URL)
    description_regex = r'"description":\s*\W(null|[^"]*)'  
    descriptions = re.findall(description_regex, raw_data)  
    return descriptions


def get_all_coordinates() -> tuple:
    
    # fetch part
    raw_data = fetch_raw_data(URL)
    coordinate_regex = r'"coordinates":\s\[(.\d\w*.\d*,\s\d*.\d*)\]'  # Regex to find coordinate
    coordinates = re.findall(coordinate_regex, raw_data)  # Find all matches

    # convert coordinates into list of tuples
    coordinates_floats = []
    for coord_str in coordinates:
        lon_str, lat_str = coord_str.split(',')
        lon, lat = float(lon_str), float(lat_str)
        coordinates_floats.append((lon, lat))
    return coordinates_floats


def get_all_geo_local_area() -> str:
    raw_data = fetch_raw_data(URL)
    geo_local_area_regex = r'"geo_local_area":\s*"([^"]*)"'
    geo_local_area = re.findall(geo_local_area_regex, raw_data)  # Find all matches
    return geo_local_area

