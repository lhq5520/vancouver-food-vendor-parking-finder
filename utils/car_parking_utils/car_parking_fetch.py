'''
VanStreet Parking
@WeifanLi

get all spcified data for car parking from parking_meter
'''

import re
from ..raw_data_fetch import fetch_raw_data

URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parking-meters/exports/json?lang=en&timezone=America%2FLos_Angeles"


# fetch data

def get_all_meterhead() -> str:
    try:
        raw_data = fetch_raw_data(URL)
    except Exception as e:
        print(f"Error fetching raw data: {e}")
        return []

    try:
        meterhead_regex = r'"meterhead":\s*.([^"]*).'  # Regex to find meter IDs
        meterheads = re.findall(meterhead_regex, raw_data)  # Find all matches
        return meterheads
    except re.error as e:
        print(f"Regex error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def get_all_meter_id() -> str:
    raw_data = fetch_raw_data(URL)
    meter_id_regex = r'"meterid": "(\w+)"'  # Regex to find meter IDs
    meter_ids = re.findall(meter_id_regex, raw_data)  # Find all matches
    return meter_ids


def get_all_coordinates() -> tuple:
    raw_data = fetch_raw_data(URL)
    coordinate_regex = r'"coordinates":\s\[(.\d\w*.\d*,\s\d*.\d*)\]'  # Regex to find coordinate
    coordinates = re.findall(coordinate_regex, raw_data)  # Find all matches
    return coordinates


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

# ------------------below get time limit at different time-----------------


# get Time Limit Mon-Fri 9AM to 6PM
def get_all_time_limit_mf_9a_6p():
    raw_data = fetch_raw_data(URL)
    time_limit_regex = r't_mf_9a_6p":\s*\W(null|[^"]*)'
    time_limits = re.findall(time_limit_regex, raw_data)  # Find all matches
    return time_limits


# get Time Limit Mon-Fri 6PM to 10PM
def get_all_time_limit_mf_6p_10():
    raw_data = fetch_raw_data(URL)
    time_limit_regex = r'"t_mf_6p_10":\s*\W(null|[^"]*)'
    time_limits = re.findall(time_limit_regex, raw_data)  # Find all matches
    return time_limits


# get Time Limit Sat 9AM to 6PM
def get_all_time_limit_sa_9a_6p():
    raw_data = fetch_raw_data(URL)
    time_limit_regex = r'"t_sa_9a_6p":\s*\W(null|[^"]*)'
    time_limits = re.findall(time_limit_regex, raw_data)  # Find all matches
    return time_limits


# get Time Limit Sat 6PM to 10PM
def get_all_time_limit_sa_6p_10():
    raw_data = fetch_raw_data(URL)
    time_limit_regex = r'"t_sa_6p_10":\s*\W(null|[^"]*)'
    time_limits = re.findall(time_limit_regex, raw_data)  # Find all matches
    return time_limits


# get Time Limit Sun 9AM to 6PM
def get_all_time_limit_su_9a_6p():
    raw_data = fetch_raw_data(URL)
    time_limit_regex = r'"t_su_9a_6p":\s*\W(null|[^"]*)'
    time_limits = re.findall(time_limit_regex, raw_data)  # Find all matches
    return time_limits


# get Time Limit Sun 6PM to 10PM
def get_all_time_limit_su_6p_10():
    raw_data = fetch_raw_data(URL)
    time_limit_regex = r'"t_su_6p_10":\s*\W(null|[^"]*)'
    time_limits = re.findall(time_limit_regex, raw_data)  # Find all matches
    return time_limits

# ---------------------below get different rate at different time ---------------------


# get rate Mon-Fri 9AM to 6PM
def get_all_rate_mf_9a_6p():
    raw_data = fetch_raw_data(URL)
    rate_regex = r'"r_mf_9a_6p":\s*"([^"]*)"'
    rates = re.findall(rate_regex, raw_data)  # Find all matches
    return rates


# get rate Mon-Fri 6PM to 10PM
def get_all_rate_mf_6p_10():
    raw_data = fetch_raw_data(URL)
    rate_regex = r'"r_mf_6p_10":\s*"([^"]*)"'
    rates = re.findall(rate_regex, raw_data)  # Find all matches
    return rates


# get rate Saturady 9AM to 6PM
def get_all_rate_sa_9a_6p():
    raw_data = fetch_raw_data(URL)
    rate_regex = r'"r_sa_9a_6p":\s*"([^"]*)"'
    rates = re.findall(rate_regex, raw_data)  # Find all matches
    return rates


# get rate Saturady 6PM to 10PM
def get_all_rate_sa_6p_10():
    raw_data = fetch_raw_data(URL)
    rate_regex = r'"r_sa_6p_10":\s*"([^"]*)"'
    rates = re.findall(rate_regex, raw_data)  # Find all matches
    return rates


# get rate Sunday 9AM to 6PM
def get_all_rate_su_9a_6p():
    raw_data = fetch_raw_data(URL)
    rate_regex = r'"r_su_9a_6p":\s*"([^"]*)"'
    rates = re.findall(rate_regex, raw_data)  # Find all matches
    return rates


# get rate Sunday 6PM to 10PM
def get_all_rate_su_6p_10():
    raw_data = fetch_raw_data(URL)
    rate_regex = r'"r_su_6p_10":\s*"([^"]*)"'
    rates = re.findall(rate_regex, raw_data)  # Find all matches
    return rates
