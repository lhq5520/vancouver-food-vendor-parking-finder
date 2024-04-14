'''
VanStreet Parking
@WeifanLi

This class is 
'''
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
from views.gui_manager import *

def main_menu():
    '''
    incomplete menu
    '''
    print("\nWelcome to the Parking Info for food vendor Menu!")
    print("1. View all parking info")
    print("2. View all food vendor")
    print("3. look up parking info by geo local area")
    print("4. search parking for food vendor based on specified features")
    print("5. view random 10 parking spot info")
    print("....under-development.....")
    print("6. Exit")


def display_all_food_vendors(food_vendor_data):
    for food_vendor in food_vendor_data:
        append_to_display_area(str(food_vendor))


def display_all_parking_info(car_parking_data):
    for parking_info in car_parking_data:
        append_to_display_area(str(parking_info))


def display_10_random_car_parking_info(random_number_list, car_parking_data):
    '''
    print random 10 objects from the list
    '''
    for random_number in random_number_list:
        print(car_parking_data[random_number])


def display_list_of_objects(list_of_objects):
    if isinstance(list_of_objects, str):
        append_to_display_area(str(list_of_objects))
    else:
        for objects in list_of_objects:
            append_to_display_area(str(objects))

# --------------------- Below for GUI------------------------




