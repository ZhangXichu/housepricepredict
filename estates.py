import re
from scrapper import remove_spaces


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
    has_loggia: bool
    has_basement: bool

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

        pattern = re.compile(r'Hospoda:.*\((.*) m\)', re.DOTALL)
        self.dist_pub = re.findall(pattern, self.raw_data)[0]

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
                num_value = float(remove_spaces(num_value_str))
            else:
                num_value = int(remove_spaces(num_value_str))
            return num_value
        except AttributeError:
            print("overall price not found")
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
            print("overall price not found")
        return None


class Apartment(Estate):
    floor: int

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.floor = self.get_numerical_value(r'Podlaží: (.*). podlaží', is_float=False)
