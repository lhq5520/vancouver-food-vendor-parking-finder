'''

'''
from utils.data_fetch import create_parking_objects
from utils.data_fetch import create_food_vendor_objects
from math import radians, cos, sin, asin, sqrt
import pandas as pd

FIRST_ELEMENT = 0
SECOND_ELEMENT = 1


# -------------------- get all informations ----------------------

def get_all_parking_info():
    parking_info_all = create_parking_objects()
    return parking_info_all


def get_all_food_vendor_info():
    food_vendor_info_all = create_food_vendor_objects()
    return food_vendor_info_all


# -------------------- search specific data ----------------------
def find_car_parking_by_geo_local_area(geo_local_area, car_parking_list):
    search_result = []
    for car_parking in car_parking_list:
        if car_parking.geo_local_area == geo_local_area:
            search_result.append(car_parking)
    if search_result:
        return search_result
    else:
        return "\nUnable to find specified geo local area"


def find_food_vendor_by_geo_local_area(geo_local_area, food_vendor_list):
    search_result = []
    for food_vendor in food_vendor_list:
        if food_vendor.geo_local_area == geo_local_area:
            search_result.append(food_vendor)
    if search_result:
        return search_result
    else:
        return "\nUnable to find specified food_vendor by geo local area"


def find_food_vendor_by_description(description, food_vendor_list):
    search_result = []
    for food_vendor in food_vendor_list:
        if food_vendor.description == description:
            search_result.append(food_vendor)
    if search_result:
        return search_result
    else:
        return "\nUnable to find specified food_vendor by description"


def find_food_vendor_by_key(key, food_vendor_list):
    search_result = []
    for food_vendor in food_vendor_list:
        if food_vendor.key == key:
            search_result.append(food_vendor)
    if search_result:
        return search_result
    else:
        return "\nUnable to find specified food_vendor by key"


def find_food_vendor_based_on_user_preference(geo_local_area,
                                              description,
                                              food_vendor_list):
    final_search_result = []
    first_temp_search_result = []

    for food_vendor in food_vendor_list:
        if food_vendor.geo_local_area == geo_local_area:
            first_temp_search_result.append(food_vendor)

    for food_vendor in first_temp_search_result:
        if food_vendor.description == description:
            final_search_result.append(food_vendor)

    return final_search_result


def find_nearest_parking_based_on_vendor(specified_food_vendor, parking_spot, user_input_distance):
    vendors_coordinate = []
    for food_vendor in specified_food_vendor:
        vendor_coordinate = food_vendor.coordinate
        vendors_coordinate.append(vendor_coordinate)

    all_parking_spot = get_all_parking_info()

    nearest_parking_spot = []
    for parking_spot in all_parking_spot:
        distance = haversine_formula(vendors_coordinate[FIRST_ELEMENT][FIRST_ELEMENT], vendors_coordinate[FIRST_ELEMENT][SECOND_ELEMENT], 
                                     parking_spot.coordinates[FIRST_ELEMENT], parking_spot.coordinates[SECOND_ELEMENT])
        if distance < user_input_distance:
            nearest_parking_spot.append(parking_spot)
    return nearest_parking_spot


# -------------------- utils function ----------------------
def haversine_formula(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees).
    """
    # Convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    radius = 6371 # Radius of earth in kilometers. 3956 for miles. 
    distance = c * radius
    return distance


def create_list_of_carparking_dictionaries(list_of_carparking_objects):
    list_of_carparking_dict = []
    for object in list_of_carparking_objects:
        carparking_dict = {'meter_id': object.meter_id,
                           'paybyphone_id': object.paybyphone_id,
                           'meterhead': object.meterhead,
                           'time_in_effect': object.time_in_effect,
                           'credicard': object.creditcard,
                           'geo_local_area': object.geo_local_area,
                           'lon': object.coordinates[0],
                           'lat': object.coordinates[1]
                           }
        list_of_carparking_dict.append(carparking_dict)
    return list_of_carparking_dict


def create_list_of_foodvendor_dictionaries(list_of_foodvendor_objects):
    list_of_foodvendor_dict = []
    for object in list_of_foodvendor_objects:
        food_vendor_dict = {'key': object.key,
                            'business_name': object.business_name,
                            'description': object.description,
                            'coordinate': object.coordinate,
                            'geo_local_area': object.geo_local_area
                            }
        list_of_foodvendor_dict.append(food_vendor_dict)
    return list_of_foodvendor_dict


def create_list_of_dictionaries(list_of_dictionaries):
    df = pd.DataFrame(list_of_dictionaries)
    return df


def get_unique_values_from_column(data_frame, column_name):
    """
    Removes duplicate rows based on a specified column and returns a list of unique values from that column.

    Args:
    data_frame (pd.DataFrame): The DataFrame to process.
    column_name (str): The name of the column to check for unique values.

    Returns:
    list: A list containing unique values from the specified column.
    """
    if column_name in data_frame.columns:
        drop_duplicate_column = data_frame.drop_duplicates(subset=[column_name])
        unique_values_list = drop_duplicate_column[column_name].tolist()
        return unique_values_list
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
