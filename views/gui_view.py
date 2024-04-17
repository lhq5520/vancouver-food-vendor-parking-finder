'''
CS5001 Spring 2024 Final Project
@WeifanLi

function that used to input or output with user's interaction
'''

from views.gui_manager import append_to_display_area


def display_list_of_objects(list_of_objects):
    """
    Purpose: Display each object from a list of objects in the display area, converting each object to a string.

    Parameters:
        list_of_objects (list or str): A list of objects or a single string object to be displayed.

    Returns: None
    """
    if isinstance(list_of_objects, str):
        append_to_display_area(str(list_of_objects))
    else:
        for objects in list_of_objects:
            append_to_display_area(str(objects))


def prompt_user_to_do():
    """
    Purpose: Display a message in the display area instructing the user to use the pop-up window for selections or inputs.

    Parameters: None

    Returns: None
    """
    append_to_display_area("Please use the pop-up window to select/input the answer. Closing window will result in defult Selection.")


def pop_title_look_up_parking_by_geo():
    """
    Purpose: Provide the title for the pop-up window used to look up parking by geographical area.

    Parameters: None

    Returns:
        str: The title for the parking lookup pop-up window.
    """
    pop_title = "Look Up Parking Info by Geo Area"
    return pop_title


def pop_prompt_look_up_parking_by_geo():
    """
    Purpose: Provide a prompt for selecting a geographical area in the parking lookup pop-up window.

    Parameters: None

    Returns:
        str: The prompt for selecting a geographical area.
    """
    pop_title = "Please Select the Following Geo Local Area in the Drop Down Menu to Search Parking"
    return pop_title


def pop_title_locate_food_vendor_by_geo():
    """
    Purpose: Provide the title for the pop-up window used to look up food vendors by geographical area.

    Parameters: None

    Returns:
        str: The title for the food vendor lookup pop-up window.
    """
    pop_title = "First: Look Up food vendor by Geo Area"
    return pop_title


def pop_prompt_locate_food_vendor_by_geo():
    """
    Purpose: Provide a prompt for selecting a geographical area in the food vendor lookup pop-up window.

    Parameters: None

    Returns: 
        str: The prompt for selecting a geographical area to locate food vendors.
    """
    pop_title = "Please Select the Following Geo Local Area in the Drop Down Menu to Locate Food Vendors"
    return pop_title


def pop_title_locate_food_vendor_by_type():
    """
    Purpose: Provide the title for the pop-up window used to look up food vendors by type.

    Parameters: None

    Returns:
        str: The title for the food vendor type lookup pop-up window.
    """
    pop_title = "Second: Look Up food vendor by Vendors' Type"
    return pop_title


def pop_prompt_locate_food_vendor_by_type():
    """
    Purpose: Provide a prompt for selecting the type of vendors in the food vendor lookup pop-up window.

    Parameters: None

    Returns:
        str: The prompt for selecting types of vendors.
    """
    pop_title = "Please Select the Following Types of Vendors in the Drop Down Menu to further Locate Food Vendors"
    return pop_title


def pop_title_locate_food_vendor_by_key():
    """
    Purpose: Provide the title for the pop-up window used to look up food vendors by a unique key.

    Parameters: None

    Returns:
        str: The title for the food vendor key lookup pop-up window.
    """
    pop_title = "Third: Look Up food vendor by unique key"
    return pop_title


def pop_prompt_locate_food_vendor_by_key():
    """
    Purpose: Provide a prompt for selecting a food vendor by unique key in the pop-up window.

    Parameters: None

    Returns:
        str: The prompt for selecting a vendor by key.
    """
    pop_title = "Please Refer Main Menu to Select the Following Types of Vendors in the Drop Down Menu to finalize Food Vendors selection"
    return pop_title


def pop_title_generate_map():
    """
    Purpose: Generate a title for the popup window used in the final step of locating a food vendor by unique key.

    Parameters:
        None

    Returns:
        str: The title for the popup window.
    """
    pop_title = "Finally: Look Up food vendor by unique key"
    return pop_title


def pop_prompt_generate_map():
    """
    Purpose: Create a prompt message for the popup window where the user specifies the maximum distance to find parking.

    Parameters:
        None

    Returns:
        str: The prompt message for the popup window.
    """
    pop_title = "Please Specify the Longest Distance in KM That You Like to Find the Parking Spot: \n(0.1 is recommended since more distance more info on the map)"
    return pop_title


def generate_generate_map_distance_options():
    """
    Purpose: Generate a list of distance options in kilometers that the user can select from.

    Parameters:
        None

    Returns:
        list: A list of float numbers representing distance options.
    """
    options = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    return options


def message_box_no_result_prompt():
    """
    Purpose: Provide a message for the messagebox that will be displayed if no matching result is found.

    Parameters:
        None

    Returns:
        str: The message indicating no matched result was found.
    """
    message = "It Seems There Is No Matched Result for Specific Food Vendor in Selected Area. Please Try Again"
    return message


def message_box_no_result_title():
    """
    Purpose: Provide a title for the messagebox that appears when no results are found.

    Parameters:
        None

    Returns:
        str: The title for the messagebox indicating no results.
    """
    message = "No Result Found!"
    return message
