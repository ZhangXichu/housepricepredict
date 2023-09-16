import re
from scrapper import remove_spaces


def get_overall_price(raw_data):
    """
    function extracts the overall price from the raw data
    :param raw_data:
    :return:
    """
    price_finder = re.search(r'Celková cena: (.*?) Kč', raw_data)
    try:
        overall_price_str = price_finder.group(1)
        overall_price = int(remove_spaces(overall_price_str))
        print(overall_price)
        return overall_price
    except:
        print("overall price not found")
    finally:
        return None
