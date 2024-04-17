'''
CS5001 Spring 2024 Final Project
@WeifanLi

Unitest for Car_Parking class that used to represent models
use python -m unittest tests.Car_Parking_unitest to run
'''
from models.Car_Parking import CarParking
import unittest


class TestCarParking(unittest.TestCase):
    def setUp(self):
        # Create a CarParking object to use in all tests
        self.car_parking = CarParking(
            meter_id="123",
            paybyphone_id="456",
            meterhead="North",
            time_in_effect="9 AM - 5 PM",
            creditcard=True,
            geo_local_area="Downtown",
            coordinates="34.0522 N, 118.2437 W"
        )

    def test_initialization(self):
        # Test that the object is initialized with the correct attributes
        self.assertEqual(self.car_parking.meter_id, "123")
        self.assertEqual(self.car_parking.paybyphone_id, "456")
        self.assertEqual(self.car_parking.meterhead, "North")
        self.assertEqual(self.car_parking.time_in_effect, "9 AM - 5 PM")
        self.assertTrue(self.car_parking.creditcard)
        self.assertEqual(self.car_parking.geo_local_area, "Downtown")
        self.assertEqual(self.car_parking.coordinates, "34.0522 N, 118.2437 W")

    def test_str_method(self):
        # Test the __str__ method
        expected_output = (
            "Meter ID: 123\n"
            "PayByPhone ID: 456\n"
            "Meter Head: North\n"
            "Time in Effect: 9 AM - 5 PM\n"
            "Credit Card Accepted: Yes\n"
            "Geographical Area: Downtown\n"
            "Coordinates: 34.0522 N, 118.2437 W\n"
        )
        self.assertEqual(str(self.car_parking), expected_output)

    def test_compare_geo_area(self):
        # Test that compare_geo_area works for both matching and non-matching cases
        self.assertTrue(self.car_parking.compare_geo_area("Downtown"))  # Should be True
        self.assertFalse(self.car_parking.compare_geo_area("Uptown"))   # Should be False
