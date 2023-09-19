import re
import numpy as np
from scrapper import remove_spaces, extract_digits
import sys


class Estate:
    raw_data: str
    apartment_type: str
    building_state: str
    ownership: str
    overall_price: float
    usable_area: float
    loggia_area: float
    basement_area: float
    dist_pub: float  # distance to the nearest pub
    dist_bus: float
    dist_atm: float
    dist_train: float
    dist_tram: float
    dist_shop: float
    dist_rest: float  # restaurant
    has_loggia: bool
    has_basement: bool
    near_pub: bool
    near_bus: bool
    near_atm: bool
    near_train: bool
    near_tram: bool
    near_shop: bool
    near_rest: bool

    def __init__(self, raw_data):
        self.raw_data = raw_data

        self.overall_price = self.get_numerical_value(r'Celková cena: (.*?) Kč')
        self.usable_area = self.get_numerical_value(r'Užitná plocha: (.*?) m2')
        self.apartment_type = self.get_text_value(r'Stavba: (.*)')
        self.building_state = self.get_text_value(r'Stav objektu: (.*)')
        self.ownership = self.get_text_value(r'Vlastnictví: (.*)')
        self.loggia_area = self.get_numerical_value(r'Lodžie: (.*) m2')
        self.basement_area = self.get_numerical_value(r'Sklep: (.*) m2')
        self.has_loggia = "Lodžie".upper() in raw_data.upper()
        self.has_basement = "Sklep".upper() in raw_data.upper()

        self.near_pub, self.dist_pub = self.check_nearby(r'Hospoda:.*?\(([0-9]*) m\)') # non-greedy pattern match
        self.near_bus, self.dist_bus = self.check_nearby(r'Bus MHD:.*?\(([0-9]*) m\)')
        self.near_atm, self.dist_atm = self.check_nearby(r'Bankomat:.*?\(([0-9]*) m\)')
        self.near_train, self.dist_train = self.check_nearby(r'Vlak:.*?\(([0-9]*) m\)')
        self.near_tram, self.dist_tram = self.check_nearby(r'Tram:.*?\(([0-9]*) m\)')
        self.near_shop, self.dist_shop = self.check_nearby(r'Obchod:.*?\(([0-9]*) m\)')
        self.near_rest, self.dist_rest = self.check_nearby(r'Restaurace:.*?\(([0-9]*) m\)')

    def check_nearby(self, context):
        """
        function checks if the estate is close to a given facility
        :param context:
        :return:
        """
        pattern = re.compile(context, re.DOTALL)
        distance = re.findall(pattern, self.raw_data)
        # print(self.raw_data)
        if distance:
            return True, float(re.findall(pattern, self.raw_data)[0])
        else:
            return False, 1000000

    def get_numerical_value(self, context, is_float=True):
        """
        function extracts numerical value from raw data
        :param is_float:
        :param context: pattern, where to find the text value
        :return:
        """
        price_finder = re.search(context, self.raw_data)
        try:
            num_value_str = price_finder.group(1)
            if is_float:
                num_value_str_strip = remove_spaces(num_value_str)
                try:
                    num_value = float(remove_spaces(num_value_str_strip))
                except ValueError:
                    # in case the string contains other symbols then digits
                    num_value_str_strip = extract_digits(num_value_str_strip)
                    num_value = float(remove_spaces(num_value_str_strip))
            else:
                num_value = int(remove_spaces(num_value_str))
            return num_value
        except AttributeError:
            print("target in context " + context + " not found")
        return None

    def get_text_value(self, context):
        """
        function extracts text value from raw data
        :param context: pattern, where to find the text value
        :return:
        """
        price_finder = re.search(context, self.raw_data)
        try:
            text_value = price_finder.group(1)
            text_value = text_value.strip()
            return text_value
        except AttributeError:
            print("target in context " + context + " not found")
        return None


class Apartment(Estate):
    floor: int

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.floor = self.get_numerical_value(r'Podlaží: (.*). podlaží', is_float=False)



