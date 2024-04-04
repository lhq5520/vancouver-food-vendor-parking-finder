from models.Car_Parking import CarParking
from utils.car_parking_utils.car_parking_parse import *


def create_car_parking():
    meter_ids = parsed_meter_id()
    paybyphone_ids = parsed_pay_phone_id()
    meterheads = parsed_meterhead()
    time_in_effects = parsed_timeineffee()
    creditcards = parsed_creditcard_support_status()
    geo_local_areas = parsed_geo_local_area()
    coordinates = parsed_coordinates()

    r_mf_9a_6ps = parsed_r_mf_9a_6p()
    r_mf_6p_10s = parsed_r_mf_6p_10()
    r_sa_9a_6ps = parsed_r_sa_9a_6p()
    r_sa_6p_10s = parsed_r_sa_6p_10()
    r_su_9a_6ps = parsed_r_su_9a_6p()
    r_su_6p_10s = parsed_r_su_6p_10()

    t_mf_9a_6ps = parsed_t_mf_9a_6p()
    t_mf_6p_10s = parsed_t_mf_6p_10()
    t_sa_9a_6ps = parsed_t_sa_9a_6p()
    t_sa_6p_10s = parsed_t_sa_6p_10()
    t_su_9a_6ps = parsed_t_su_9a_6p()
    t_su_6p_10s = parsed_t_su_6p_10()

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
        r_mf_9a_6p = r_mf_9a_6ps[i]
        r_mf_6p_10 = r_mf_6p_10s[i]
        r_sa_9a_6p = r_sa_9a_6ps[i]
        r_sa_6p_10 = r_sa_6p_10s[i]
        r_su_9a_6p = r_su_9a_6ps[i]
        r_su_6p_10 = r_su_6p_10s[i]
        t_mf_9a_6p = t_mf_9a_6ps[i]
        t_mf_6p_10 = t_mf_6p_10s[i]
        t_sa_9a_6p = t_sa_9a_6ps[i]
        t_sa_6p_10 = t_sa_6p_10s[i]
        t_su_9a_6p = t_su_9a_6ps[i]
        t_su_6p_10 = t_su_6p_10s[i]

        # create a CarParking object with these variables
        car_parking = CarParking(
            meter_id, paybyphone_id, meterhead, time_in_effect, creditcard, geo_local_area,
            coordinate, r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10,
            t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10
        )

        car_parking_list.append(car_parking)

    return car_parking_list


def find_car_parking_by_meter_id(meter_id, car_parking_list):
    for car_parking in car_parking_list:
        if car_parking.meter_id == meter_id:
            return car_parking
    return "Unable to find specified meter id"


def find_car_parking_by_geo_local_area(geo_local_area, car_parking_list):
    search_result = []
    for car_parking in car_parking_list:
        if car_parking.geo_local_area == geo_local_area:
            search_result.append(car_parking)
    if search_result:
        return search_result
    else:
        return "Unable to find specified meter id"
