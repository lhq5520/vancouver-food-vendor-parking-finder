'''
CS5001 Spring 2024 Final Project
@WeifanLi

data_dashboard - the controller

It creates objects and directs the control flow between view and model
'''

from utils.model_helper import *
from utils.data_fetch import *
from models.Car_Parking import CarParking
from models.Food_Vendor import FoodVendor

from views.gui_view import *
from views.parking_map import *
from views.bar_graph import *
from views.gui_manager import *
import tkinter as tk
from tkinter import messagebox

import requests


CARPARKING_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parking-meters/exports/json?lang=en&timezone=America%2FLos_Angeles"
FOOD_VENDOR_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/food-vendors/exports/json?lang=en&timezone=America%2FLos_Angeles"


def create_food_vendor_objects():
    '''
    Purpose: Create a list of FoodVendor objects from parsed food vendor data.
    This function validates the consistency of data lengths and raises
    an IndexError if there is a mismatch.
    Additionally, it handles exceptions from data fetching functions and rethrows them with more context.

    Parameters:
        no parameters

    Returns:
        food_vendor_list (list): A list of FoodVendor objects created from the data.

    Raises:
        ValueError: If an error occurs during the fetching of data.
        IndexError: If the data attributes lists are not of equal length.
    '''
    # store all the lists of attributes
    business_names = get_all_businessname()
    descriptions = get_all_description()
    geo_local_areas = get_all_food_vendor_geo_local_area()
    coordinates = get_all_food_vendor_coordinates()
    keys = get_all_key()

    if not (len(keys) == len(business_names) == len(descriptions)
            == len(geo_local_areas) == len(coordinates)):
        raise IndexError("Mismatch in lengths of data attributes in create_food_vendor_objects().")

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


def create_parking_objects():
    '''
    Purpose: Create and return a list of CarParking objects from
    parsed parking meter data. Raises an IndexError
    if there is a mismatch in the lengths of data attributes.

    Parameters:
        no parameters

    Returns:
        car_parking_list (list): A list of CarParking objects created from the data.

    Raises:
        IndexError: If the data attributes lists are not of equal length.
    '''
    # store all the lists of attributes
    meter_ids = get_all_meter_id()
    paybyphone_ids = get_all_pay_phone_id()
    meterheads = get_all_meterhead()
    time_in_effects = get_all_timeineffee()
    creditcards = get_all_creditcard_support_status()
    geo_local_areas = get_all_geo_local_area()
    coordinates = get_all_coordinates()

    if not (len(meter_ids) == len(paybyphone_ids) == len(meterheads) ==
            len(time_in_effects) == len(creditcards) == len(geo_local_areas)
            == len(coordinates)):
        raise IndexError("Data lists are not of equal length in create_parking_objects.")

    # load objects into a list
    car_parking_list = []
    for i in range(len(meter_ids)):
        # Access each item by index
        meter_id = meter_ids[i]
        paybyphone_id = paybyphone_ids[i]
        meterhead = meterheads[i]
        time_in_effect = time_in_effects[i]
        creditcard = creditcards[i]
        geo_local_area = geo_local_areas[i]
        coordinate = coordinates[i]

        # create a CarParking object with these variables
        car_parking = CarParking(
            meter_id, paybyphone_id, meterhead, time_in_effect, creditcard,
            geo_local_area, coordinate
        )
        car_parking_list.append(car_parking)
    return car_parking_list


# click view all parking info
def run_view_all_parking_info():
    '''
    Purpose: Clear the display area and show all parking information available.

    Parameters: None

    Returns: None

    Raises: None
    '''
    run_clear_display()
    parking_info = create_parking_objects()
    parking_dict = create_list_of_carparking_dictionaries(parking_info)
    parking_data_frame = create_list_of_dictionaries(parking_dict)
    parking_counts = parking_data_frame['geo_local_area'].value_counts()

    display_list_of_objects(parking_info)
    show_food_vendor_bar_graph(parking_counts)


# click view all food vendor info
def run_view_all_food_vendor():
    '''
    Purpose: Clear the display area and show all food vendor information.

    Parameters: None

    Returns: None

    Raises: None
    '''
    run_clear_display()
    food_vendors = create_food_vendor_objects()
    food_vendor_dict = create_list_of_foodvendor_dictionaries(food_vendors)
    food_vendor_data_frame = create_list_of_dictionaries(food_vendor_dict)
    vendor_counts = food_vendor_data_frame['geo_local_area'].value_counts()

    display_list_of_objects(food_vendors)
    show_food_vendor_bar_graph(vendor_counts)


# click Look Up Parking Info by Geo Area
def run_look_up_parking_by_geo():
    '''
    Purpose: Allows the user to look up parking information by geographical area through a GUI dropdown select.

    Parameters: None

    Returns: None

    Raises:
        ValueError: If no parking information is available for the selected geographical area.
    '''
    run_clear_display()
    # generate for the unique select drop down options
    prompt_user_to_do()

    parking_info = create_parking_objects()
    parking_dict = create_list_of_carparking_dictionaries(parking_info)
    parking_data_frame = create_list_of_dictionaries(parking_dict)
    unique_geo_generation = get_unique_values_from_column(parking_data_frame, "geo_local_area")

    pop_up_title = pop_title_look_up_parking_by_geo()
    pop_up_prompt = pop_prompt_look_up_parking_by_geo()
    dropdown_select_geo = gui_input_from_drop_down_select(pop_up_title, unique_geo_generation, pop_up_prompt)
    result = find_car_parking_by_geo_local_area(dropdown_select_geo, parking_info)
    display_list_of_objects(result)


# click Search Nearest Parking Spot By Preferred Food Vendor
def run_find_nearet_parking_spot():
    '''
    Purpose: Locates the nearest parking spots to a selected food vendor based on user preferences entered through GUI.

    Parameters: None

    Returns: None

    Raises:
        ValueError: If no matching food vendor or parking spots are found within the specified distance.
    '''
    prompt_user_to_do()

    run_clear_display()
    # get all data results
    food_vendors = create_food_vendor_objects()
    # get user to decide which restaurant to choose from
    food_vendor_dict = create_list_of_foodvendor_dictionaries(food_vendors)
    food_vendor_data_frame = create_list_of_dictionaries(food_vendor_dict)
    unique_geo_generation = get_unique_values_from_column(food_vendor_data_frame, "geo_local_area")

    first_pop_up_title = pop_title_locate_food_vendor_by_geo()
    first_pop_up_prompt = pop_prompt_locate_food_vendor_by_geo()
    user_input_geo_local_area = gui_input_from_drop_down_select(first_pop_up_title, unique_geo_generation, first_pop_up_prompt)

    unique_foodtype_generation = get_unique_values_from_column(food_vendor_data_frame, "description")

    second_pop_up_title = pop_title_locate_food_vendor_by_type()
    second_pop_up_prompt = pop_prompt_locate_food_vendor_by_type()
    user_input_vendor_description = gui_input_from_drop_down_select(second_pop_up_title, unique_foodtype_generation, second_pop_up_prompt)

    first_result = find_food_vendor_based_on_user_preference(user_input_geo_local_area,
                                                user_input_vendor_description,
                                                food_vendors)
    if not first_result:
        message = message_box_no_result_prompt()
        title = message_box_no_result_title()
        setup_messagebox("Error", title, message)
    display_list_of_objects(first_result)

    # based on user's choice to select specific food vendor
    first_result_dict = create_list_of_foodvendor_dictionaries(first_result)
    first_result_data_frame = create_list_of_dictionaries(first_result_dict)
    unique_key_generation = get_unique_values_from_column(first_result_data_frame, "key")

    third_pop_up_title = pop_title_locate_food_vendor_by_key()
    third_pop_up_prompt = pop_prompt_locate_food_vendor_by_key()
    user_choose_vendor = gui_input_from_drop_down_select(third_pop_up_title, unique_key_generation, third_pop_up_prompt)
    final_result = find_food_vendor_by_key(user_choose_vendor, first_result)
    display_list_of_objects(final_result)

    # calculate the nearest parking spot
    parking_spots = create_parking_objects()
    forth_pop_up_title = pop_title_generate_map()
    forth_pop_up_prompt = pop_prompt_generate_map()
    user_choose_distance = generate_generate_map_distance_options()
    user_defined_distance = float(gui_input_from_drop_down_select(forth_pop_up_title, user_choose_distance, forth_pop_up_prompt))
    nearest_parking = find_nearest_parking_based_on_vendor(final_result, parking_spots, user_defined_distance, parking_spots)

    data_frame = create_list_of_carparking_dictionaries(nearest_parking)
    display_parking_spot_map(data_frame)


def run_clear_display():
    '''
    Purpose: Clears the display area in the GUI to prepare for new output.

    Parameters: None

    Returns: None

    Raises: None
    '''
    clear_display_area()


def exit_app(root):
    '''
    Purpose: Exits the application by closing the GUI window and terminating the process.

    Parameters:
        root (Tk): The root window of the Tkinter application.

    Returns: None

    Raises: None
    '''

    root.quit()
    root.destroy()
    quit()


def main():
    try:
        root = tk.Tk()
        setup_root(root)

        frame = setup_frame(root)

        # Setup the display area using the function from gui_manager
        setup_display_area(frame)

        # Buttons for different actions
        setup_buttons(frame, run_view_all_parking_info, run_view_all_food_vendor,
                    run_look_up_parking_by_geo, run_find_nearet_parking_spot, run_clear_display, exit)
        root.mainloop()
    except FileNotFoundError as fnf_error:
        print("File not found error:", fnf_error)
        messagebox.showerror("File Not Found", f"An essential file is missing: {fnf_error}")
    except PermissionError as pe_error:
        print("Permission error:", pe_error)
        messagebox.showerror("Permission Error", f"Permission denied: {pe_error}")
    except ValueError as ve_error:
        print("Value error:", ve_error)
        messagebox.showerror("Value Error", f"Invalid data encountered: {ve_error}")
    except TypeError as te_error:
        print("Type error:", te_error)
        messagebox.showerror("Type Error", f"Type mismatch or invalid type used: {te_error}")
    except requests.HTTPError as http_error:
        print("HTTP error:", http_error)
        messagebox.showerror("HTTP Error", f"HTTP request failed with status {http_error.response.status_code}: {http_error}")
    except Exception as e:
        print("An error occurred:", e)
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
