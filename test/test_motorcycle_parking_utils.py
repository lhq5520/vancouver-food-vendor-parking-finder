'''
unitest will be handled in milestone 2
'''

from utils.motorcycle_parking_utils.motorcycle_parking_parse import *


# visualize meter_id fetched
def test_get_all_motorcycle_coordinates():
    counter = 0
    for items in get_all_coordinates():
        print(items)
        print(type(items))
        counter += 1
    print(f"total coordinates fetched: {counter}")


def test_get_all_motorcycle_parking_type():
    counter = 0
    for items in get_all_parking_type():
        print(items)
        print(type(items))
        counter += 1
    print(f"total parking type fetched: {counter}")


def test_get_all_motorcycle_r_mf_9a_6p():
    counter = 0
    for items in parsed_r_mf_9a_6p():
        print(items)
        print(type(items))
        counter += 1
    print(f"total r_mf_9a_6p fetched: {counter}")