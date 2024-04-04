'''
unitest will be handled in milestone 2
'''
from models.Motorcycle_Parking import MotorcycleParking
from utils.motorcycle_parking_utils.motorcycle_parking_parse import *


def test_create_motorcycle_parking():
    parking_types = parsed_parking_type()
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
    motorcycle_parking_list = []
    for i in range(len(parking_types)):
        # Access each item by index
        parking_type = parking_types[i]
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
        car_parking = MotorcycleParking(
            parking_type, time_in_effect, creditcard, geo_local_area,
            coordinate, r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10,
            t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10
        )

        motorcycle_parking_list.append(car_parking)

    print(motorcycle_parking_list[223])
