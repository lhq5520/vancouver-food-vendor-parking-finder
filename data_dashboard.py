from views.car_parking_view import *
from utils.car_parking_utils.car_parking_load import *

def main():
    try:
        is_running = True
        while is_running == True:
            main_menu()
            choice = user_choice()

            if choice == "1": # search all lists of object by meter_id
                # Ex. B42239 is a valid meter_id
                meter_id = get_car_parking_by_meter_id()
                parking_spot = get_all_parking_spot_info()
                parking_spot_info = find_car_parking_by_meter_id(meter_id, parking_spot)
                print(parking_spot_info)
                print("\n")

            elif choice == "2": # search all lists of object by pay_by_phone_id
                # Ex. Downtown is valid
                paybyphone_id = get_car_parking_by_geo_local_area()
                parking_spot = get_all_parking_spot_info()
                parking_spot_info = find_car_parking_by_geo_local_area(paybyphone_id, parking_spot)
                for parking_spot in parking_spot_info:
                    print(parking_spot)
                    print("\n")

            elif choice == "3":
                display_10_random_car_parking_info()

            elif choice == "4":
                is_running = False

            else:
                print("Invalid choice, please select 1, 2, 3, or 4")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
