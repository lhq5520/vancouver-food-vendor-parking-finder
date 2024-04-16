'''
CS5001 Spring 2024 Final Project
@WeifanLi

Food_Vendor class that used to represent models of food vendors in vancouver
'''


class FoodVendor():
    '''
    Represent a food vendor with comprehensive attributes
    such as a unique key, business name, description, coordinates, and geographical area.
    This class provides methods for representing the food vendor as a string
    '''

    def __init__(self, key, business_name, description, coordinate,
                 geo_local_area):
        self.key = key
        self.business_name = business_name
        self.description = description
        self.coordinate = coordinate
        self.geo_local_area = geo_local_area

    def __str__(self):
        return (f"key: {self.key}\n"
                f"Business Name: {self.business_name}\n"
                f"Description: {self.description}\n"
                f"Coordinates: {self.coordinate}\n"
                f"Geographical Area: {self.geo_local_area}\n")

    def is_same_vendor(self, other):
        if not isinstance(other, FoodVendor):
            return False
        return self.key == other.key

    def is_matched_key(self, user_input_value):
        if self.key.lower() == user_input_value.lower():
            return True
        else:
            return False
