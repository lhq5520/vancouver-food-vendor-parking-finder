'''
CS5001 Spring 2024 Final Project
@WeifanLi

Unitest for model_helper.py
use python -m unittest tests.model_helper_unitest to run
'''
import unittest
from models.Car_Parking import CarParking
from models.Food_Vendor import FoodVendor
from utils.model_helper import *
import pandas as pd

class TestFunctionalities(unittest.TestCase):
    def setUp(self):
        self.car_parkings = [
            CarParking("001", "101", "North", "24/7", True, "Downtown", (34.0522, -118.2437)),
            CarParking("002", "102", "South", "10 AM - 8 PM", False, "Uptown", (40.7128, -74.0060))
        ]
        self.food_vendors = [
            FoodVendor("f001", "Gourmet Pizza", "Delicious gourmet pizza", (34.0522, -118.2437), "Downtown"),
            FoodVendor("f002", "Sushi Place", "Authentic sushi dishes", (40.7128, -74.0060), "Uptown")
        ]
        self.data_frame = pd.DataFrame([{'column_name': 'test'}])

    def test_find_car_parking_by_geo_local_area(self):
        result = find_car_parking_by_geo_local_area("Downtown", self.car_parkings)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].meter_id, "001")

    def test_find_food_vendor_by_geo_local_area(self):
        result = find_food_vendor_by_geo_local_area("Uptown", self.food_vendors)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].key, "f002")

    def test_find_food_vendor_by_description(self):
        result = find_food_vendor_by_description("Delicious gourmet pizza", self.food_vendors)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].business_name, "Gourmet Pizza")

    def test_find_food_vendor_by_key(self):
        result = find_food_vendor_by_key("f001", self.food_vendors)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].key, "f001")

    def test_find_food_vendor_based_on_user_preference(self):
        result = find_food_vendor_based_on_user_preference("Downtown", "Delicious gourmet pizza", self.food_vendors)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].key, "f001")

    def test_find_nearest_parking_based_on_vendor(self):
        # Assume that the food vendor and a nearby parking are at the same coordinates for simplicity in this test case.
        result = find_nearest_parking_based_on_vendor([self.food_vendors[0]], None, 5, self.car_parkings)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].meter_id, "001")

    def test_haversine_formula(self):
        distance = haversine_formula(34.0522, -118.2437, 34.0522, -118.2437)
        self.assertEqual(distance, 0)

    def test_create_list_of_carparking_dictionaries(self):
        result = create_list_of_carparking_dictionaries(self.car_parkings)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['meter_id'], '001')

    def test_create_list_of_foodvendor_dictionaries(self):
        result = create_list_of_foodvendor_dictionaries(self.food_vendors)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['key'], 'f001')

    def test_create_list_of_dictionaries(self):
        dictionaries = [{'key': 'value1'}, {'key': 'value2'}]
        df = create_list_of_dictionaries(dictionaries)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_get_unique_values_from_column(self):
        unique_values = get_unique_values_from_column(self.data_frame, 'column_name')
        self.assertEqual(len(unique_values), 1)
        self.assertIn('test', unique_values)
