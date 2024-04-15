'''
VanStreet Parking
@WeifanLi

get all spcified data for car parking from parking_meter
and
format data from regular expression to tailored class
'''
import requests
import re
from models.Car_Parking import CarParking
from models.Food_Vendor import FoodVendor
from data_dashboard import CARPARKING_URL, FOOD_VENDOR_URL


def fetch_raw_data(url):
    '''
    Fetch parking data from the given URL and return cleaned and structured data.
    '''
    # Sending a GET request to the URL
    response = requests.get(url)
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.text  # get raw data(String)
        return data
    else:
        raise requests.HTTPError(f"Failed to fetch data, HTTP status: {response.status_code}")


# -----------------car_parking_fetch--------------------
# fetch car data
def get_all_meterhead() -> str:
    raw_data = fetch_raw_data(CARPARKING_URL)
    meterhead_regex = r'"meterhead":\s*.([^"]*).'  # Regex to find meter IDs
    meterheads = re.findall(meterhead_regex, raw_data)  # Find all matches
    if not meterheads:
        raise ValueError("No meterheads found in the data.")
    return meterheads


def get_all_meter_id() -> str:
    raw_data = fetch_raw_data(CARPARKING_URL)
    meter_id_regex = r'"meterid": "(\w+)"'  # Regex to find meter IDs
    meter_ids = re.findall(meter_id_regex, raw_data)  # Find all matches
    if not meter_ids:
        raise ValueError("No meter IDs found in the data.")
    return meter_ids


def get_all_coordinates() -> tuple:
    # fetch part
    raw_data = fetch_raw_data(CARPARKING_URL)
    coordinate_regex = r'"coordinates":\s\[(.\d\w*.\d*,\s\d*.\d*)\]'  # Regex to find coordinate
    coordinates = re.findall(coordinate_regex, raw_data)  # Find all matches
    if not coordinates:
        raise ValueError("No coordinates found in the data.")

    # format part
    try:
        coordinates_floats = []
        for coord_str in coordinates:
            lon_str, lat_str = coord_str.split(',')
            lon, lat = float(lon_str), float(lat_str)
            coordinates_floats.append((lon, lat))
    except ValueError as e:
        raise ValueError("Error converting car parking coordinates to float: " + str(e))
    return coordinates_floats


def get_all_pay_phone_id() -> str:
    raw_data = fetch_raw_data(CARPARKING_URL)
    pay_phone_regex = r'"pay_phone":\s*.(\w*).'  
    pay_phones = re.findall(pay_phone_regex, raw_data)  # Find all matches
    if not pay_phones:
        raise ValueError("No paybyphone ID found in the data.")
    return pay_phones


def get_all_creditcard_support_status() -> str:
    raw_data = fetch_raw_data(CARPARKING_URL)
    creditcard_support_status_regex = r'"creditcard":\s*.(\w*).'  
    creditcard_support_status = re.findall(creditcard_support_status_regex, raw_data)  # Find all matches
    if not creditcard_support_status:
        raise ValueError("No creditcard_support status found in the data.")
    return creditcard_support_status


def get_all_geo_local_area() -> str:
    raw_data = fetch_raw_data(CARPARKING_URL)
    geo_local_area_regex = r'"geo_local_area":\s*"([^"]*)"'
    geo_local_area = re.findall(geo_local_area_regex, raw_data)  # Find all matches
    if not geo_local_area:
        raise ValueError("No geo local area found in the data.")
    return geo_local_area


def get_all_timeineffee() -> str:
    raw_data = fetch_raw_data(CARPARKING_URL)
    timeineffe_regex = r'"timeineffe":\s.([^"]*).'
    # timeineffe_regex = r'"timeineffe":\s*(?:"METER IN EFFECT:\s*(\d{1,2}:\d{2} [AP]M TO \d{1,2}:\d{2} [AP]M)"|null)'
    timeineffe = re.findall(timeineffe_regex, raw_data)  # Find all matches
    if not timeineffe:
        raise ValueError("No time in effect information found in the data.")
    return timeineffe


def create_parking_objects():
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


def create_list_of_carparking_dictionaries():
    list_of_carparking_object = create_parking_objects()
    if not list_of_carparking_object:
        raise ValueError("No parking data available to create dictionaries.")
    list_of_carparking_dict = []
    for object in list_of_carparking_object:
        carparking_dict = {'meter_id': object.meter_id,
                           'paybyphone_id': object.paybyphone_id,
                           'meterhead': object.meterhead,
                           'time_in_effect': object.time_in_effect,
                           'credicard': object.creditcard,
                           'geo_local_area': object.geo_local_area,
                           'coordinate': object.coordinates}
        list_of_carparking_dict.append(carparking_dict)
    return list_of_carparking_dict


# -----------------food_vendor_fetch--------------------
def get_all_key() -> str:
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    key_regex = r'"key":\s*\W(null|[^"]*)'
    key = re.findall(key_regex, raw_data)
    if not key:
        raise ValueError("No keys found in the data.")
    return key


def get_all_businessname() -> str:
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    businessname_regex = r'"business_name":\s*\W(null|[^"]*)'
    businessnames = re.findall(businessname_regex, raw_data)
    if not businessnames:
        raise ValueError("No business names found in the data.")
    return businessnames


def get_all_description() -> str:
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    description_regex = r'"description":\s*\W(null|[^"]*)'
    descriptions = re.findall(description_regex, raw_data)
    if not descriptions:
        raise ValueError("No descriptions found in the data.")
    return descriptions


def get_all_food_vendor_geo_local_area() -> str:
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    geo_local_area_regex = r'"geo_localarea":\s*"([^"]*)"'
    geo_local_area = re.findall(geo_local_area_regex, raw_data)  # Find all matches
    if not geo_local_area:
        raise ValueError("No geographical local areas found in the data.")
    return geo_local_area


def get_all_food_vendor_coordinates() -> tuple:
    # fetch part
    raw_data = fetch_raw_data(FOOD_VENDOR_URL)
    coordinate_regex = r'"coordinates":\s\[(.\d\w*.\d*,\s\d*.\d*)\]'  # Regex to find coordinate
    coordinates = re.findall(coordinate_regex, raw_data)  # Find all matches
    if not coordinates:
        raise ValueError("No coordinates found in the data.")

    # convert coordinates into list of tuples
    try:
        coordinates_floats = []
        for coord_str in coordinates:
            lon_str, lat_str = coord_str.split(',')
            lon, lat = float(lon_str), float(lat_str)
            coordinates_floats.append((lon, lat))
    except ValueError as e:
        raise ValueError(f"Error converting food vendor coordinates: {str(e)}")
    return coordinates_floats


def create_food_vendor_objects():
    try:
    # store all the lists of attributes
        business_names = get_all_businessname()
        descriptions = get_all_description()
        geo_local_areas = get_all_food_vendor_geo_local_area()
        coordinates = get_all_food_vendor_coordinates()
        keys = get_all_key()
    except ValueError as e:
        raise ValueError(f"Error fetching data in create_food_vendor_objects: {str(e)}")

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
