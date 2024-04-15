'''
VanStreet Parking
@WeifanLi

This class is 
'''

from views.gui_manager import append_to_display_area


def display_list_of_objects(list_of_objects):
    if isinstance(list_of_objects, str):
        append_to_display_area(str(list_of_objects))
    else:
        for objects in list_of_objects:
            append_to_display_area(str(objects))


def prompt_user_to_do():
    append_to_display_area("Please use the pop-up window to select/input the answer")


def prompt_carparking_distance():
    distance = "Please specify the longest distance in KM that you like to find the parking spot: "
    return distance


def pop_title_look_up_parking_by_geo():
    pop_title = "Look Up Parking Info by Geo Area"
    return pop_title


def pop_prompt_look_up_parking_by_geo():
    pop_title = "Please Select the Following Geo Local Area in the Drop Down Menu to Search Parking"
    return pop_title


def pop_title_locate_food_vendor_by_geo():
    pop_title = "First: Look Up food vendor by Geo Area"
    return pop_title


def pop_prompt_locate_food_vendor_by_geo():
    pop_title = "Please Select the Following Geo Local Area in the Drop Down Menu to Locate Food Vendors"
    return pop_title


def pop_title_locate_food_vendor_by_type():
    pop_title = "Second: Look Up food vendor by Vendors' Type"
    return pop_title


def pop_prompt_locate_food_vendor_by_type():
    pop_title = "Please Select the Following Types of Vendors in the Drop Down Menu to further Locate Food Vendors"
    return pop_title


def pop_title_locate_food_vendor_by_key():
    pop_title = "Finally: Look Up food vendor by unique key"
    return pop_title


def pop_prompt_locate_food_vendor_by_key():
    pop_title = "Please Refer Main Menu to Select the Following Types of Vendors in the Drop Down Menu to finalize Food Vendors selection"
    return pop_title
