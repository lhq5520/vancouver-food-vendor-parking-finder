'''

VanStreet Parking
@WeifanLi

This class is 
'''

import random
from utils.car_parking_utils.car_parking_load import *


def get_all_parking_spot_info():
    car_parking_data = create_car_parking()
    return car_parking_data


def main_menu():
        '''
        incomplete menu
        '''
        print("\nWelcome to the Parking Info Menu!")
        print("1. Look up parking info by Meter ID")
        print("2. Look up parking info by Geo local area")
        print("3. view random 10 parking spot info")
        print("....under-development.....")
        print("4. Exit")


def user_choice():
    choice = input("Enter your choice (1-4): ")
    return choice


def display_10_random_car_parking_info():
    '''
    print random 10 objects from the list
    '''
    car_parking_data = get_all_parking_spot_info()

    random_number_list = []
    for i in range(10):
        random_number = random.randrange(0, 6863)
        random_number_list.append(random_number)

    for random_number in random_number_list:
        print(car_parking_data[random_number])


def get_car_parking_by_meter_id():
    meter_id = input("Enter Meter ID: ")
    return meter_id


def get_car_parking_by_geo_local_area():
    paybyphone_id = input("Enter a geo local area: ")
    return paybyphone_id
