from views.input_view import *
from views.output_view import *
from utils.model_helper import *
from views.data_frame import *
from views.map import *


def run_find_nearet_parking_spot():
    food_vendors = get_all_food_vendor_info()
    user_input_geo_local_area = input_geo_local_area()
    user_input_vendor_description = input_description_of_food()

    first_result = find_food_vendor_based_on_user_preference(user_input_geo_local_area,
                                                user_input_vendor_description,
                                                food_vendors)
    display_list_of_objects(first_result)

    user_choose_vendor = input_final_selection_by_key()
    final_result = find_food_vendor_by_key(user_choose_vendor, first_result)
    display_list_of_objects(final_result)

    # calculate the nearest parking spot
    parking_spots = get_all_parking_info()
    user_defined_distance = input_carparking_distance()
    nearest_parking = find_nearest_parking_based_on_vendor(final_result, parking_spots, user_defined_distance)
    # display_list_of_objects(nearest_parking)

    data_frame = create_list_of_carparking_dictionaries(nearest_parking)
    display_list_of_dictionaries(data_frame)
    return data_frame


def main():
    is_running = True
    while is_running == True:
        main_menu()
        choice = user_choice()

        if choice == "1": # search all lists of object by meter_id
            # Ex. B42239 is a valid meter_id
            parking_info = get_all_parking_info()
            display_all_parking_info(parking_info)

        elif choice == "2":
            food_vendors = get_all_food_vendor_info()
            display_all_food_vendors(food_vendors)

        elif choice == "3": # search all lists of object by geo_local_area
            # Ex. Downtown is valid
            parking_info = get_all_parking_info()
            user_input_geo_local_area = input_geo_local_area()
            result = find_car_parking_by_geo_local_area(user_input_geo_local_area, parking_info)
            display_list_of_objects(result)

        elif choice == "4":
            df = run_find_nearet_parking_spot()
            view_map(df)
            

        elif choice == "5":
            random_index_list = generate_10_random_index()
            parking_info  = get_all_parking_info()
            display_10_random_car_parking_info(random_index_list, parking_info)


        elif choice == "6":
            is_running = False

        else:
            print("Invalid choice, please select 1, 2, 3, or 4")


if __name__ == '__main__':
    main()
