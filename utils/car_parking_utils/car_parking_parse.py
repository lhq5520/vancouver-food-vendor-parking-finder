'''
VanStreet Parking
@WeifanLi

format data from regular expression to tailored class
'''

from .car_parking_fetch import *


def parsed_meterhead():
    meterhead = get_all_meterhead()
    return meterhead


def parsed_meter_id():
    meter_id = get_all_meter_id()
    return meter_id


def parsed_coordinates():
    raw_coordinates = get_all_coordinates()
    coordinates_floats = []
    for coord_str in raw_coordinates:
        lon_str, lat_str = coord_str.split(',')
        lon, lat = float(lon_str), float(lat_str)
        coordinates_floats.append((lon, lat))
    return coordinates_floats


def parsed_pay_phone_id():
    pay_phone_id = get_all_pay_phone_id()
    return pay_phone_id


def parsed_creditcard_support_status():
    creditcard_support_status = get_all_creditcard_support_status()
    return creditcard_support_status


def parsed_geo_local_area():
    geo_local_area = get_all_geo_local_area()
    return geo_local_area


def parsed_timeineffee():
    timeineffee_raw = get_all_timeineffee()
    return timeineffee_raw


# ----------------------- time limit ------------------ #
def parsed_t_mf_9a_6p():
    raw_t_mf_9a_6p = get_all_time_limit_mf_9a_6p()
    return raw_t_mf_9a_6p


def parsed_t_mf_6p_10():
    raw_t_mf_6p_10 = get_all_time_limit_mf_6p_10()
    return raw_t_mf_6p_10


def parsed_t_sa_9a_6p():
    raw_t_sa_9a_6p = get_all_time_limit_sa_9a_6p()
    return raw_t_sa_9a_6p


def parsed_t_sa_6p_10():
    raw_t_sa_6p_10 = get_all_time_limit_sa_6p_10()
    return raw_t_sa_6p_10


def parsed_t_su_9a_6p():
    raw_t_su_9a_6p = get_all_time_limit_su_9a_6p()
    return raw_t_su_9a_6p


def parsed_t_su_6p_10():
    raw_t_su_6p_10 = get_all_time_limit_su_6p_10()
    return raw_t_su_6p_10


# ----------------------- rate ---------------- #
def parsed_r_mf_9a_6p():
    raw_r_mf_9a_6p = get_all_rate_mf_9a_6p()
    parking_rate_floats = []
    for item in raw_r_mf_9a_6p:
        parking_rate = float(item.split("$")[1])
        parking_rate_floats.append(parking_rate)
    return parking_rate_floats


def parsed_r_mf_6p_10():
    raw_r_mf_6p_10 = get_all_rate_mf_6p_10()
    parking_rate_floats = []
    for item in raw_r_mf_6p_10:
        parking_rate = float(item.split("$")[1])
        parking_rate_floats.append(parking_rate)
    return parking_rate_floats


def parsed_r_sa_9a_6p():
    raw_r_sa_9a_6p = get_all_rate_sa_9a_6p()
    parking_rate_floats = []
    for item in raw_r_sa_9a_6p:
        parking_rate = float(item.split("$")[1])
        parking_rate_floats.append(parking_rate)
    return parking_rate_floats


def parsed_r_sa_6p_10():
    raw_r_sa_6p_10 = get_all_rate_sa_6p_10()
    parking_rate_floats = []
    for item in raw_r_sa_6p_10:
        parking_rate = float(item.split("$")[1])
        parking_rate_floats.append(parking_rate)
    return parking_rate_floats


def parsed_r_su_9a_6p():
    raw_r_su_9a_6p = get_all_rate_su_9a_6p()
    parking_rate_floats = []
    for item in raw_r_su_9a_6p:
        parking_rate = float(item.split("$")[1])
        parking_rate_floats.append(parking_rate)
    return parking_rate_floats


def parsed_r_su_6p_10():
    raw_r_su_6p_10 = get_all_rate_su_6p_10()
    parking_rate_floats = []
    for item in raw_r_su_6p_10:
        parking_rate = float(item.split("$")[1])
        parking_rate_floats.append(parking_rate)
    return parking_rate_floats
