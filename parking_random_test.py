'''
VanStreet Parking
@WeifanLi

'''

from test.test_Car_Parking import test_create_car_parking
from test.test_car_parking_utils import test_get_all_coordinates
from test.test_motorcycle_parking_utils import *
from test.test_Motorcycle_Parking import test_create_motorcycle_parking

def main():
    # test_create_car_parking()
    # test_get_all_coordinates()
    # test_get_all_motorcycle_coordinates()
    # test_get_all_parking_type()
    # test_create_motorcycle_parking()
    test_create_motorcycle_parking()
if __name__ == '__main__':
    main()