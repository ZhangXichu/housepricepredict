from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
import httplib2
import requests
import mechanicalsoup
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
from math import floor
import codecs
from urllib.parse import urlparse
import os
import time


def remove_spaces(string):
    return string.replace(" ", "")


def get_id_from_url(address):
    o = urlparse(address)
    return os.path.split(o.path)[1]

# TODO: crate functions for parsing the data in a saparate file


def get_all_ids(url_sub, driver, page_num):
    """
    function acquires all the links to the ads with there ids,
    and writes those links in a txt file, one link per line
    :param url_sub: url of the webpage of apartment info or house info
    :param driver: browser driver object
    :param page_num: total amount of pages the list of estate ads span
    :return:None
    """
    # get all the ids of the ads

    out_file_name = "raw.txt"

    # try:
    #     os.remove(out_file_name)
    # except OSError:
    #     pass
    #
    with codecs.open(out_file_name, "a", "utf-8") as targetFile:

        for i in range(703, page_num):
            if i >= 2:
                url = url_sub + "?strana=" + str(i)
            else:
                url = url_sub
            driver.get(url)

            print("Current page: " + str(i))

            # get all the links on a page
            elements = driver.find_elements(By.TAG_NAME, "a")

            id_links = set()
            if elements:
                for x in elements:
                    try:
                        href = x.get_attribute('href')
                        if (href is not None) and ("detail/prodej/byt/" in href):
                            id_links.add(href)
                    except:
                        pass

            for x in id_links:
                targetFile.write(x)
                targetFile.write("\n")

            time.sleep(5)

    targetFile.close()


def load_raw_data(driver):
    out_file_name = "raw.txt"

    try:
        os.remove(out_file_name)
    except OSError:
        pass

    file = open('raw_lst.txt', 'r')

    with codecs.open(out_file_name, "a", "utf-8") as targetFile:
        while True:
            ad_link = file.readline().strip()
            if not ad_link:
                break

            print("link: " + ad_link)

            # get all the links on a page
            driver.get(ad_link)

            apartment_info = driver.find_element(By.XPATH, "/html/body").text

            targetFile.write(apartment_info)
            targetFile.write("\n")

    targetFile.close()


if __name__ == '__main__':
    root_url = "https://www.sreality.cz/"

    url_apartment = root_url + "/hledani/prodej/byty"
    url_house = root_url + "/hledani/domy"

    driver = webdriver.Chrome()

    driver.get(url_apartment)

    # calculate number of pages
    apartments_lst_info = driver.find_element(By.XPATH, "/html/body").text
    n_per_page = 20
    n_total = re.search(r'Zobrazujeme výsledky 1–20 z celkem (.*?) nalezených', apartments_lst_info).group(1)
    n_total = int(remove_spaces(n_total))
    n_pages = floor(n_total / n_per_page)

    # get_all_ids(url_apartment, driver, n_pages)
    load_raw_data(driver)



