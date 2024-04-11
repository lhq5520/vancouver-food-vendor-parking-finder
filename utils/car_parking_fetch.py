'''
VanStreet Parking
@WeifanLi

get all spcified data for car parking from parking_meter
and
format data from regular expression to tailored class
'''

import re
from utils.raw_data_fetch import fetch_raw_data
from models.Car_Parking import CarParking

URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parking-meters/exports/json?lang=en&timezone=America%2FLos_Angeles"


# fetch data

def get_all_meterhead() -> str:
    raw_data = fetch_raw_data(URL)
    meterhead_regex = r'"meterhead":\s*.([^"]*).'  # Regex to find meter IDs
    meterheads = re.findall(meterhead_regex, raw_data)  # Find all matches
    return meterheads


def get_all_meter_id() -> str:
    raw_data = fetch_raw_data(URL)
    meter_id_regex = r'"meterid": "(\w+)"'  # Regex to find meter IDs
    meter_ids = re.findall(meter_id_regex, raw_data)  # Find all matches
    return meter_ids


def get_all_coordinates() -> tuple:
    # fetch part
    raw_data = fetch_raw_data(URL)
    coordinate_regex = r'"coordinates":\s\[(.\d\w*.\d*,\s\d*.\d*)\]'  # Regex to find coordinate
    coordinates = re.findall(coordinate_regex, raw_data)  # Find all matches

    # format part
    coordinates_floats = []
    for coord_str in coordinates:
        lon_str, lat_str = coord_str.split(',')
        lon, lat = float(lon_str), float(lat_str)
        coordinates_floats.append((lon, lat))
    return coordinates_floats


def get_all_pay_phone_id() -> str:
    raw_data = fetch_raw_data(URL)
    pay_phone_regex = r'"pay_phone":\s*.(\w*).'  
    pay_phones = re.findall(pay_phone_regex, raw_data)  # Find all matches
    return pay_phones


def get_all_creditcard_support_status() -> str:
    raw_data = fetch_raw_data(URL)
    creditcard_support_status_regex = r'"creditcard":\s*.(\w*).'  
    creditcard_support_status = re.findall(creditcard_support_status_regex, raw_data)  # Find all matches
    return creditcard_support_status


def get_all_geo_local_area() -> str:
    raw_data = fetch_raw_data(URL)
    geo_local_area_regex = r'"geo_local_area":\s*"([^"]*)"'
    geo_local_area = re.findall(geo_local_area_regex, raw_data)  # Find all matches
    return geo_local_area


def get_all_timeineffee() -> str:
    raw_data = fetch_raw_data(URL)
    timeineffe_regex = r'"timeineffe":\s.([^"]*).'
    # timeineffe_regex = r'"timeineffe":\s*(?:"METER IN EFFECT:\s*(\d{1,2}:\d{2} [AP]M TO \d{1,2}:\d{2} [AP]M)"|null)'
    timeineffe = re.findall(timeineffe_regex, raw_data)  # Find all matches
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
