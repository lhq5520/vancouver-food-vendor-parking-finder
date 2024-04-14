import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
from views.gui_manager import *


def user_choice():
    choice = input("Enter your choice (1-6): ")
    return choice


def prompt_user_to_do():
    global display_area
    append_to_display_area("Please use the pop-up window to select/input the answer")


def input_description_of_food():
    vendor_description = "Enter types of food you want: "
    return vendor_description


def input_vendor_key():
    vendor_key = input("Enter the key of the food vendor: ")
    return vendor_key


def input_final_selection_by_key():
    vendor_key = input("Please enter the key from above list to confirm final food vendor selection: ")
    return vendor_key


def prompt_carparking_distance():
    distance = "Please specify the longest distance in KM that you like to find the parking spot: "
    return distance

# --------------------- Below for GUI------------------------


