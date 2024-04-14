from views.input_view import *
from views.output_view import *
from utils.model_helper import *
from views.data_frame import *
from views.map import *

import tkinter as tk

# click view all parking info
def run_view_all_parking_info():
    parking_info = get_all_parking_info()
    display_all_parking_info(parking_info)


# click view all food vendor info
def run_view_all_food_vendor():
    food_vendors = get_all_food_vendor_info()
    display_all_food_vendors(food_vendors)


# click Look Up Parking Info by Geo Area
def run_look_up_parking_by_geo():
    # generate for the unique select drop down options
    prompt_user_to_do()

    parking_info = get_all_parking_info()
    parking_dict = create_list_of_carparking_dictionaries(parking_info)
    data_frame = create_list_of_dictionaries(parking_dict)
    unique_column = get_unique_values_from_column(data_frame, "geo_local_area")
    user_input_geo_local_area = gui_input_from_list("select", unique_column)
    result = find_car_parking_by_geo_local_area(user_input_geo_local_area, parking_info)
    display_list_of_objects(result)

# def run_view_ten_random_parking():
#     random_index_list = generate_10_random_index()
#     parking_info  = get_all_parking_info()
#     display_10_random_car_parking_info(random_index_list, parking_info)


def run_find_nearet_parking_spot():

    # get all data results
    food_vendors = get_all_food_vendor_info()
    # get user to decide which restaurant to choose from
    foodvendor_dict = create_list_of_foodvendor_dictionaries(food_vendors)
    foodvendor_data_frame = create_list_of_dictionaries(foodvendor_dict)
    unique_geo_column = get_unique_values_from_column(foodvendor_data_frame, "geo_local_area")
    user_input_geo_local_area = gui_input_from_list("Area", unique_geo_column)

    unique_foodtype_column = get_unique_values_from_column(foodvendor_data_frame, "description")
    user_input_vendor_description = gui_input_from_list("What do you want to eat?", unique_foodtype_column)

    first_result = find_food_vendor_based_on_user_preference(user_input_geo_local_area,
                                                user_input_vendor_description,
                                                food_vendors)
    display_list_of_objects(first_result)

    # based on user's choice to select specific food vendor
    first_result_dict = create_list_of_foodvendor_dictionaries(first_result)
    first_result_data_frame = create_list_of_dictionaries(first_result_dict)
    unique_key_column = get_unique_values_from_column(first_result_data_frame, "key")

    user_choose_vendor = user_input_geo_local_area = gui_input_from_list("Food Vendor", unique_key_column)
    final_result = find_food_vendor_by_key(user_choose_vendor, first_result)
    display_list_of_objects(final_result)

    # calculate the nearest parking spot
    parking_spots = get_all_parking_info()
    user_defined_distance = float(gui_input_from_prompt(prompt_carparking_distance()))
    nearest_parking = find_nearest_parking_based_on_vendor(final_result, parking_spots, user_defined_distance)

    data_frame = create_list_of_carparking_dictionaries(nearest_parking)
    display_list_of_dictionaries(nearest_parking)
    display_parking_spot_map(data_frame)


def run_clear_display():
    clear_display_area()


def main():
    root = tk.Tk()
    root.title("Parking Info System")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Setup the display area using the function from gui_manager
    setup_display_area(frame)

    # Buttons for different actions
    tk.Button(frame, text="View All Parking Info", command=run_view_all_parking_info).pack(fill=tk.X)
    tk.Button(frame, text="View All Food Vendors", command=run_view_all_food_vendor).pack(fill=tk.X)
    tk.Button(frame, text="Look Up Parking Info by Geo Area", command=run_look_up_parking_by_geo).pack(fill=tk.X)
    tk.Button(frame, text="Search Nearest Parking Spot By Prefered Food Vendor", command=run_find_nearet_parking_spot).pack(fill=tk.X)
    tk.Button(frame, text="Clear Display", command=run_clear_display).pack(fill=tk.X)
    tk.Button(frame, text="Exit", command=root.quit).pack(fill=tk.X)
    root.mainloop()

if __name__ == '__main__':
    main()
