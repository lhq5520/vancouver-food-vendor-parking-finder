'''
CS5001 Spring 2024 Final Project
@WeifanLi

function that search for the information
'''
from math import radians, cos, sin, asin, sqrt
import pandas as pd

FIRST_ELEMENT = 0
SECOND_ELEMENT = 1
TWO = 2
EARTH_RADIUS = 6371


# -------------------- search specific data ----------------------
def find_car_parking_by_geo_local_area(geo_local_area, car_parking_list):
    """
    Purpose: Search for car parking by geographical local area from
    a list of car parking objects.

    Parameters:
        geo_local_area (str): The geographical area to search within.
        car_parking_list (list): A list of car parking objects to search through.

    Returns: List of car parking objects matching the
    specified geographical area or a message indicating no results found.

    Raises:
        TypeError: If car_parking_list is not a list.
        ValueError: If car_parking_list is empty.
    """

    if not isinstance(car_parking_list, list):
        raise TypeError("car_parking_list must be a list.")
    if not car_parking_list:
        raise ValueError("car_parking_list is empty and has no data to search through.")

    search_result = []
    for car_parking in car_parking_list:
        if car_parking.geo_local_area == geo_local_area:
            search_result.append(car_parking)
    if search_result:
        return search_result
    else:
        return "\nUnable to find specified geo local area"


def find_food_vendor_by_geo_local_area(geo_local_area, food_vendor_list):
    """
    Purpose: Search for food vendors by geographical local area.

    Parameters:
        geo_local_area (str): The geographical area to search within.
        food_vendor_list (list): A list of food vendor objects to search through.

    Returns: List of food vendor objects that match the
    specified geographical area or a message indicating no results found.

    Raises:
        TypeError: If food_vendor_list is not a list.
        ValueError: If food_vendor_list is empty.
    """
    if not isinstance(food_vendor_list, list):
        raise TypeError("food_vendor_list must be a list.")
    if not food_vendor_list:
        raise ValueError("food_vendor_list is empty.")

    search_result = []
    for food_vendor in food_vendor_list:
        if food_vendor.geo_local_area == geo_local_area:
            search_result.append(food_vendor)
    if search_result:
        return search_result
    else:
        return "\nUnable to find specified food_vendor by geo local area"


def find_food_vendor_by_description(description, food_vendor_list):
    """
    Purpose: Search for food vendors by description.

    Parameters:
        description (str): The description to match against food vendor objects.
        food_vendor_list (list): A list of food vendor objects.

    Returns: List of food vendor objects that match 
    the specified description or a message indicating no results found.

    Raises:
        TypeError: If food_vendor_list is not a list.
        ValueError: If food_vendor_list is empty.
    """

    if not isinstance(food_vendor_list, list):
        raise TypeError("food_vendor_list must be a list.")
    if not food_vendor_list:
        raise ValueError("food_vendor_list is empty.")

    search_result = []
    for food_vendor in food_vendor_list:
        if food_vendor.description == description:
            search_result.append(food_vendor)
    if search_result:
        return search_result
    else:
        return "\nUnable to find specified food_vendor by description"


def find_food_vendor_by_key(key, food_vendor_list):
    """
    Purpose: Search for food vendors by a unique key identifier.

    Parameters:
        key (str): The unique key to search for.
        food_vendor_list (list): A list of food vendor objects.

    Returns: List of food vendor objects that match
    the specified key or a message indicating no results found.

    Raises:
        TypeError: If food_vendor_list is not a list.
        ValueError: If food_vendor_list is empty.
    """

    if not isinstance(food_vendor_list, list):
        raise TypeError("food_vendor_list must be a list.")
    if not food_vendor_list:
        raise ValueError("food_vendor_list is empty.")

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
    """
    Purpose: Filter food vendors based on user-specified geographical area
    and description.

    Parameters:
        geo_local_area (str): The geographical area to filter by.
        description (str): The description to filter by.
        food_vendor_list (list): A list of food vendor objects.

    Returns: List of food vendors that match both the
    specified geographical area and description.

    Raises:
        TypeError: If food_vendor_list is not a list.
        ValueError: If food_vendor_list is empty.
    """
    if not isinstance(food_vendor_list, list):
        raise TypeError("food_vendor_list must be a list.")
    if not food_vendor_list:
        raise ValueError("food_vendor_list is empty.")

    final_search_result = []
    first_temp_search_result = []

    for food_vendor in food_vendor_list:
        if food_vendor.geo_local_area == geo_local_area:
            first_temp_search_result.append(food_vendor)

    for food_vendor in first_temp_search_result:
        if food_vendor.description == description:
            final_search_result.append(food_vendor)

    return final_search_result


def find_nearest_parking_based_on_vendor(specified_food_vendor, parking_spot, user_input_distance, list_of_parking_obj):
    """
    Purpose: Find the nearest parking spots to a given food vendor
    within a specified distance.

    Parameters:
        specified_food_vendor (list): List of food vendor objects to find parking near.
        parking_spot (object): The parking spot object (currently unused in function body).
        user_input_distance (float): Maximum distance in kilometers to consider.
        list_of_parking_obj (list): List of parking objects to search from.

    Returns: List of parking spots within the specified distance from the food vendor.

    Raises:
        TypeError: If list_of_parking_obj is not a list or user_input_distance is not a non-negative number.
        ValueError: If list_of_parking_obj is empty.
    """
    if not isinstance(list_of_parking_obj, list):
        raise TypeError("list_of_parking_obj must be a list.")
    if not isinstance(user_input_distance, (int, float)) or user_input_distance < 0:
        raise ValueError("user_input_distance must be a non-negative number.")
    if not list_of_parking_obj:
        raise ValueError("list_of_parking_obj is empty.")

    vendors_coordinate = []
    for food_vendor in specified_food_vendor:
        vendor_coordinate = food_vendor.coordinate
        vendors_coordinate.append(vendor_coordinate)

    all_parking_spot = list_of_parking_obj

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
    Purpose: Calculate the great circle distance in kilometers
    between two points on the earth, specified in decimal degrees.

    Parameters:
        lon1 (float): Longitude of the first point.
        lat1 (float): Latitude of the first point.
        lon2 (float): Longitude of the second point.
        lat2 (float): Latitude of the second point.

    Returns: The distance between the two points in kilometers.

    Raises:
        TypeError: If any input is not a float.
        ValueError: If latitude or longitude values are out of accepted range.
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    intermediate_value = sin(dlat/TWO)**TWO + cos(lat1) * cos(lat2) * sin(dlon/TWO)**TWO
    central_angle = 2 * asin(sqrt(intermediate_value)) 
    radius = EARTH_RADIUS # Radius of earth in kilometers. 3956 for miles.
    distance = central_angle * radius
    return distance


def create_list_of_carparking_dictionaries(list_of_carparking_objects):
    """
    Purpose: Convert a list of CarParking objects into a list of dictionaries representing each parking meter with its data.

    Parameters:
        list_of_carparking_objects (list): A list of CarParking objects.

    Returns: A list of dictionaries, each representing a parking meter.

    Raises:
        ValueError: If no CarParking data is available for conversion.
        TypeError: If the input is not a list of CarParking objects.
    """

    if not list_of_carparking_objects:
        raise ValueError("No CarParking data available to convert.")
    if not isinstance(list_of_carparking_objects, list):
        raise TypeError("list_of_carparking_objects must be a list of CarParking objects.")

    list_of_carparking_dict = []
    for object in list_of_carparking_objects:
        carparking_dict = {'meter_id': object.meter_id,
                           'paybyphone_id': object.paybyphone_id,
                           'meterhead': object.meterhead,
                           'time_in_effect': object.time_in_effect,
                           'credicard': object.creditcard,
                           'geo_local_area': object.geo_local_area,
                           'lon': object.coordinates[FIRST_ELEMENT],
                           'lat': object.coordinates[SECOND_ELEMENT]
                           }
        list_of_carparking_dict.append(carparking_dict)
    return list_of_carparking_dict


def create_list_of_foodvendor_dictionaries(list_of_foodvendor_objects):
    """
    Purpose: Convert a list of FoodVendor objects into a list of dictionaries representing each vendor.

    Parameters:
        list_of_foodvendor_objects (list): A list of FoodVendor objects.

    Returns: A list of dictionaries, each representing a food vendor.

    Raises:
        ValueError: If no FoodVendor data is available for conversion.
        TypeError: If the input is not a list of FoodVendor objects.
    """
    if not list_of_foodvendor_objects:
        raise ValueError("No food vendor data available to convert.")
    if not isinstance(list_of_foodvendor_objects, list):
        raise TypeError("list_of_foodvendor_objects must be a list of FoodVendor objects.")

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
    """
    Purpose: Convert a list of dictionaries into a pandas DataFrame.

    Parameters:
        list_of_dictionaries (list): A list of dictionaries to be converted into a DataFrame.

    Returns: A pandas DataFrame created from the list of dictionaries.

    Raises:
        ValueError: If the list is empty.
    """
    if not list_of_dictionaries:
        raise ValueError("The create_list_of_dictionaries failed: list is empty.")

    df = pd.DataFrame(list_of_dictionaries)
    return df


def get_unique_values_from_column(data_frame, column_name):
    """
    Purpose: Retrieve a list of unique values from a specified column in a DataFrame.

    Parameters:
        data_frame (pd.DataFrame): The DataFrame to process.
        column_name (str): The name of the column to check for unique values.

    Returns: A list containing unique values from the specified column.

    Raises:
        TypeError: If data_frame is not a pandas DataFrame.
        ValueError: If the DataFrame is empty or the specified column does not exist.
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError("data_frame must be a pandas DataFrame.")
    if data_frame.empty:
        raise ValueError("The DataFrame is empty.")
    if column_name not in data_frame.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    if column_name in data_frame.columns:
        drop_duplicate_column = data_frame.drop_duplicates(subset=[column_name])
        unique_values_list = drop_duplicate_column[column_name].tolist()
        return unique_values_list
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
