import re
from scrapper import remove_spaces


def get_numerical_value(raw_data, context):
    """
    function extracts numerical value from raw data
    :param raw_data: string of raw data
    :param context: pattern, where to find the numerical value
    :return: int, the target numerical value; None, if not found
    """
    price_finder = re.search(context, raw_data)
    try:
        num_value_str = price_finder.group(1)
        num_value = int(remove_spaces(num_value_str))
        return num_value
    except AttributeError:
        print("overall price not found")
    return None


def get_text_value(raw_data, context):
    """
    function extracts text value from raw data
    :param raw_data: string of raw data
    :param context: pattern, where to find the text value
    :return: text valu
    """
    price_finder = re.search(context, raw_data)
    try:
        text_value = price_finder.group(1)
        text_value = text_value.strip()
        return text_value
    except AttributeError:
        print("overall price not found")
    return None


def get_overall_price(raw_data):
    """
    function extracts the overall price
    :param raw_data: string of raw data
    :return: int, overall price
    """
    return get_numerical_value(raw_data, r'Celková cena: (.*?) Kč')


def get_usable_area(raw_data):
    """
    function extracts the usable area
    :param raw_data: string of raw data
    :return: int, usable area
    """
    return get_numerical_value(raw_data, r'Užitná plocha: (.*?) m2')


def get_apartment_type(raw_data):
    """
    function extracts the type of apartment
    :param raw_data:  string of raw data
    :return: string, type of apartment
    """
    return get_text_value(raw_data, r'Stavba: (.*)')


def get_floor(raw_data):
    """
    function extracts on which floor is the apartment
    :param raw_data: string of raw data
    :return: int, overall price
    """
    return get_numerical_value(raw_data, r'Podlaží: (.*). podlaží')


def get_building_state(raw_data):
    """
    function extracts the state of the building
    :param raw_data:  string of raw data
    :return: string, the state of the building
    """
    return get_text_value(raw_data, r'Stav objektu: (.*)')


def get_ownership(raw_data):
    """
    function extracts to whom the real estate belongs
    :param raw_data:  string of raw data
    :return: string, the ownership
    """
    return get_text_value(raw_data, r'Vlastnictví: (.*)')


def get_loggia_area(raw_data):
    """
    function extracts loggia area
    :param raw_data: string of raw data
    :return: int, loggia area
    """
    return get_numerical_value(raw_data, r'Lodžie: (.*) m2')


def check_loggia(raw_data):
    """
    function checks if the estate has loggia
    :param raw_data: string of raw data
    :return: bool, true if loggia is mentioned
    """
    return "Lodžie".upper() in raw_data.upper()


def get_basement_area(raw_data):
    """
    function extracts loggia area
    :param raw_data: string of raw data
    :return: int, loggia area
    """
    return get_numerical_value(raw_data, r'Sklep: (.*) m2')


def check_basement(raw_data):
    """
    function checks if the estate has basement
    :param raw_data: string of raw data
    :return: bool, true if basement is mentioned
    """
    return "Sklep".upper() in raw_data.upper()


def dist_pub(raw_data):
    """
    function gets the distance to the nearest pub
    :param raw_data:  string of raw data
    :return: int, distance to the nearest pub
    """
    pattern = re.compile(r'Hospoda:.*\((.*) m\)', re.DOTALL)
    dist_str = re.findall(pattern, raw_data)[0]
    return int(dist_str)







