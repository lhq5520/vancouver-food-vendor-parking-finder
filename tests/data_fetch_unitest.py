'''
CS5001 Spring 2024 Final Project
@WeifanLi

Unitest for data_fetch.py
use python -m unittest tests.data_fetch_unitest to run
'''

import unittest
from unittest.mock import patch, MagicMock
import requests

# Adjust the import path to match the module structure
from utils.data_fetch import (
    fetch_raw_data, get_all_meterhead, get_all_meter_id, get_all_coordinates,
    get_all_pay_phone_id, get_all_creditcard_support_status, get_all_geo_local_area,
    get_all_timeineffee, get_all_key, get_all_businessname, get_all_description,
    get_all_food_vendor_geo_local_area, get_all_food_vendor_coordinates
)

class TestDataFetching(unittest.TestCase):

    def test_fetch_raw_data_success(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = MagicMock(status_code=200, text='Successful data fetch')
            response = fetch_raw_data('http://fakeurl.com')
            self.assertEqual(response, 'Successful data fetch')

    def test_fetch_raw_data_failure(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = MagicMock(status_code=404)
            with self.assertRaises(requests.HTTPError):
                fetch_raw_data('http://fakeurl.com')

    def test_get_all_meterhead(self):
        # Test parsing and extracting meterhead descriptions
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"meterhead": "North"}'
            result = get_all_meterhead()
            self.assertEqual(result, ["North"])

    def test_get_all_meter_id(self):
        # Test retrieving all meter IDs from the data
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"meterid": "12345"}'
            result = get_all_meter_id()
            self.assertEqual(result, ["12345"])

    def test_get_all_coordinates(self):
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"some_other_key": "some_value"}'
            with self.assertRaises(ValueError):
                get_all_coordinates()

    def test_get_all_pay_phone_id(self):
        # Test retrieving PayByPhone IDs
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"pay_phone": "98765"}'
            result = get_all_pay_phone_id()
            self.assertEqual(result, ["98765"])

    def test_get_all_creditcard_support_status(self):
        # Test extracting credit card support statuses
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"creditcard": "Yes"}'
            result = get_all_creditcard_support_status()
            self.assertEqual(result, ["Yes"])

    def test_get_all_geo_local_area(self):
        # Test extracting geographical local areas
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"geo_local_area": "Downtown"}'
            result = get_all_geo_local_area()
            self.assertEqual(result, ["Downtown"])

    def test_get_all_timeineffee(self):
        # Test retrieving time in effect information
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"timeineffe": "9 AM - 5 PM"}'
            result = get_all_timeineffee()
            self.assertEqual(result, ["9 AM - 5 PM"])

    def test_get_all_key(self):
        # Test retrieving unique keys for food vendors
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"key": "abc123"}'
            result = get_all_key()
            self.assertEqual(result, ["abc123"])

    def test_get_all_businessname(self):
        # Test extracting business names
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"business_name": "Best Burgers"}'
            result = get_all_businessname()
            self.assertEqual(result, ["Best Burgers"])

    def test_get_all_description(self):
        # Test fetching descriptions for food vendors
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"description": "Delicious gourmet burgers"}'
            result = get_all_description()
            self.assertEqual(result, ["Delicious gourmet burgers"])

    def test_get_all_food_vendor_geo_local_area(self):
        # Test extracting geographical local areas for food vendors
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"geo_localarea": "Market District"}'
            result = get_all_food_vendor_geo_local_area()
            self.assertEqual(result, ["Market District"])

    def test_get_all_food_vendor_coordinates(self):
        # Test extracting and converting geographic coordinates for food vendors
        with patch('utils.data_fetch.fetch_raw_data') as mock_fetch:
            mock_fetch.return_value = '{"some_other_key": "some_value"}'
            with self.assertRaises(ValueError):
                get_all_food_vendor_coordinates()
