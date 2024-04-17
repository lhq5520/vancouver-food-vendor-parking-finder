'''
CS5001 Spring 2024 Final Project
@WeifanLi

Unitest for Food_Vendor class that used to represent models
use python -m unittest tests.Food_Vendor_unitest to run
'''
import unittest
from models.Food_Vendor import FoodVendor


class TestFoodVendor(unittest.TestCase):
    def setUp(self):
        # Creating a FoodVendor object to be used in all the tests
        self.vendor = FoodVendor(
            key="12345",
            business_name="Gourmet Hot Dogs",
            description="Artisan hot dogs with unique toppings",
            coordinate="49.2827 N, 123.1207 W",
            geo_local_area="Downtown Vancouver"
        )

    def test_initialization(self):
        # Test that the object is initialized with correct attributes
        self.assertEqual(self.vendor.key, "12345")
        self.assertEqual(self.vendor.business_name, "Gourmet Hot Dogs")
        self.assertEqual(self.vendor.description, "Artisan hot dogs with unique toppings")
        self.assertEqual(self.vendor.coordinate, "49.2827 N, 123.1207 W")
        self.assertEqual(self.vendor.geo_local_area, "Downtown Vancouver")

    def test_str_method(self):
        # Test the __str__ method
        expected_output = (
            "key: 12345\n"
            "Business Name: Gourmet Hot Dogs\n"
            "Description: Artisan hot dogs with unique toppings\n"
            "Coordinates: 49.2827 N, 123.1207 W\n"
            "Geographical Area: Downtown Vancouver\n"
        )
        self.assertEqual(str(self.vendor), expected_output)

    def test_is_same_vendor(self):
        # Test to verify if two vendors with the same key are identified as the same
        vendor2 = FoodVendor("12345", "Another Name", "Another Description", "Coordinates", "Area")
        self.assertTrue(self.vendor.is_same_vendor(vendor2))
        # Test with a different key
        vendor3 = FoodVendor("54321", "Gourmet Hot Dogs", "Description", "Coordinates", "Area")
        self.assertFalse(self.vendor.is_same_vendor(vendor3))

    def test_is_matched_key(self):
        # Test matching key with case sensitivity
        self.assertTrue(self.vendor.is_matched_key("12345"))
        self.assertTrue(self.vendor.is_matched_key("12345"))
        self.assertFalse(self.vendor.is_matched_key("abcde"))
