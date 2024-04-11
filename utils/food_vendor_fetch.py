import re
from utils.raw_data_fetch import fetch_raw_data
from models.Food_Vendor import FoodVendor

URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/food-vendors/exports/json?lang=en&timezone=America%2FLos_Angeles"


def get_all_key() -> str:
    raw_data = fetch_raw_data(URL)
    key_regex = r'"key":\s*\W(null|[^"]*)'
    key = re.findall(key_regex, raw_data)
    return key


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


def get_all_food_vendor_geo_local_area() -> str:
    raw_data = fetch_raw_data(URL)
    geo_local_area_regex = r'"geo_localarea":\s*"([^"]*)"'
    geo_local_area = re.findall(geo_local_area_regex, raw_data)  # Find all matches
    return geo_local_area


def get_all_food_vendor_coordinates() -> tuple:
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


def create_food_vendor_objects():
    # store all the lists of attributes
    business_names = get_all_businessname()
    descriptions = get_all_description()
    geo_local_areas = get_all_food_vendor_geo_local_area()
    coordinates = get_all_food_vendor_coordinates()
    keys = get_all_key()

    # load objects into a list
    food_vendor_list = []
    for i in range(len(business_names)):
        # Access each item by index
        key = keys[i]
        business_name = business_names[i]
        description = descriptions[i]
        geo_local_area = geo_local_areas[i]
        coordinate = coordinates[i]

        # create a CarParking object with these variables
        food_vendor = FoodVendor(
            key, business_name, description, coordinate, geo_local_area
            )
        food_vendor_list.append(food_vendor)
    return food_vendor_list
