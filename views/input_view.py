

def user_choice():
    choice = input("Enter your choice (1-6): ")
    return choice


def input_meter_id():
    meter_id = input("Enter Meter ID: ")
    return meter_id


def input_geo_local_area():
    geo_local_area = input("Enter a geo local area: ")
    return geo_local_area


def input_description_of_food():
    vendor_description = input("Enter types of food you want: ")
    return vendor_description


def input_vendor_key():
    vendor_key = input("Enter the key of the food vendor: ")
    return vendor_key


def input_final_selection_by_key():
    vendor_key = input("Please enter the key from above list to confirm final food vendor selection: ")
    return vendor_key


def input_carparking_distance():
    distance = float(input("Please specify the longest distance in KM that you like to find the parking spot: "))
    return distance

