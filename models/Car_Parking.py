'''
CS5001 Spring 2024 Final Project
@WeifanLi

Car_Parking class that used to represent models
'''


class CarParking():
    '''
    Represent a car parking spot with detailed attributes like
    meter ID, PayByPhone ID, meterhead, time in effect, credit card acceptance, geographical area, and coordinates.
    This class encapsulates all relevant details of a parking spot and provides a string representation for easy viewing.
    '''

    def __init__(self, meter_id, paybyphone_id, meterhead, time_in_effect,
                 creditcard, geo_local_area, coordinates):

        # spcific data used for parking
        self.meter_id = meter_id
        self.paybyphone_id = paybyphone_id
        self.meterhead = meterhead

        self.time_in_effect = time_in_effect
        self.creditcard = creditcard
        self.geo_local_area = geo_local_area
        self.coordinates = coordinates

    def __str__(self):
        return (f"Meter ID: {self.meter_id}\n"
                f"PayByPhone ID: {self.paybyphone_id}\n"
                f"Meter Head: {self.meterhead}\n"
                f"Time in Effect: {self.time_in_effect}\n"
                f"Credit Card Accepted: {'Yes' if self.creditcard else 'No'}\n"
                f"Geographical Area: {self.geo_local_area}\n"
                f"Coordinates: {self.coordinates}\n")

    def compare_geo_area(self, geo_local_area):
        '''
        Compare the geographical area of this parking spot with another.

        Parameters:
            geo_local_area (str): user's input to compare with.

        Returns:
            bool: True if both objects are in the same geographical area, otherwise False.
        '''
        result = False
        if self.geo_local_area == geo_local_area:
            result = True
        else:
            result = False
        return result
