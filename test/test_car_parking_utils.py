
'''
unitest will be handled in milestone 2
'''
from utils.car_parking_utils.car_parking_fetch import (get_all_meter_id, get_all_coordinates, get_all_rate_mf_9a_6p, get_all_rate_mf_6p_10, get_all_rate_sa_9a_6p, get_all_rate_sa_6p_10, get_all_rate_su_9a_6p, get_all_rate_su_6p_10,
                                  get_all_time_limit_mf_9a_6p, get_all_time_limit_mf_6p_10, get_all_time_limit_sa_9a_6p, get_all_time_limit_sa_6p_10, get_all_time_limit_su_9a_6p, get_all_time_limit_su_6p_10,
                                  get_all_geo_local_area, get_all_creditcard_support_status, get_all_pay_phone_id, get_all_meterhead, get_all_timeineffee)


# visualize meter_id fetched
def test_get_all_meter_id():
    counter = 0
    for items in get_all_meter_id():
        print(items)
        print(type(items))
        counter += 1
    print(f"total meter_id fetched: {counter}")


# visualize meter_id fetched
def test_get_all_coordinates():
    counter = 0
    for items in get_all_coordinates():
        print(items)
        print(type(items))
        counter += 1
    print(f"total coordinates fetched: {counter}")

#print(get_all_coordinates())
#load data into objects

'''
parking_spots = []
for items in get_all_meterhead():
    parking_spot = ParkingSpot()
    '''

#print(get_all_time_limit())

'''
coordinates_floats = []
for coord_str in get_all_coordinates():
    lon_str, lat_str = coord_str.split(',')
    lon, lat = float(lon_str), float(lat_str)
    coordinates_floats.append((lon, lat))
    '''

'''
counter = 0
raw_t_mf_9a_6p = get_all_time_limit_mf_9a_6p()
for item in raw_t_mf_9a_6p:
    if item == "30 min":
        item = "0.5 Hr"
    if item != "No Time Limit" and item != "null" and item != "other":
        parking_limit = item.split(" ")[0]
        print(parking_limit)
        counter += 1
#print(counter)
        '''


'''
raw_r_mf_9a_6p = get_all_rate_mf_9a_6p()
counter = 0
parking_rate_floats = []
for item in raw_r_mf_9a_6p:
    parking_rate = float(item.split("$")[1])
    parking_rate_floats.append(parking_rate)

print(parking_rate_floats[0])
'''