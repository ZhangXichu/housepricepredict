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
        overall_price_str = price_finder.group(1)
        overall_price = int(remove_spaces(overall_price_str))
        return overall_price
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

