import urllib.request

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
import estates


def remove_spaces(string):
    return string.replace(" ", "")


def get_id_from_url(address):
    """
    function acquires the id of an a
    :param address:
    :return: string
    """
    o = urlparse(address)
    return os.path.split(o.path)[1]


def get_coord_from_url(address, coord='x'):
    """
    function gets the x or y coordinate from a url
    :return: float
    """
    if coord == 'x':
        pattern = r'.*?x=(.*)&y='
    else:
        pattern = r'.*&y=(.*)&z='
    try:
        pattern_finder = re.search(pattern, address)
        c = pattern_finder.group(1)
        res = float(c)
        return res
    except AttributeError:
        print("No coordinte info found")
        return None


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
    """
    function downloads html documents and images of each ad of
    a real estate
    :param driver:
    :return:
    """
    out_file_name = "raw.txt"

    try:
        os.remove(out_file_name)
    except OSError:
        pass

    file = open('raw_lst.txt', 'r')

    counter = 0
    while counter <= 30:
        ad_link = file.readline().strip()
        if not ad_link:
            break

        ad_id = get_id_from_url(ad_link)
        print("ad_id: " + ad_id)

        # get all the links on a page
        driver.get(ad_link)
        img_results = driver.find_elements(By.XPATH, "//img[contains(@src, 'sreality.png')]")

        map_results = driver.find_elements(By.XPATH, "//a[contains(@href, 'mapy.cz/?x=')]")

        img_links = set()
        for img in img_results:
            img_link = img.get_attribute('src')
            if img_link is not None:
                # print("image src: ", img_link)
                img_links.add(img_link)

        map_links = []
        for m in map_results:
            map_link = m.get_attribute('href')
            if map_link is not None:
                map_links.append(map_link)

        # print(map_links)
        m_href = map_links[0]  # the location info in stored in the first one
        longitude = get_coord_from_url(m_href, coord='x')
        latitude = get_coord_from_url(m_href, coord='y')

        i = 1
        img_concat_names = ""  # this will be stored in the database
        for img_link in img_links:
            img_name = ad_id + "_" + str(i) + ".png"
            urllib.request.urlretrieve(img_link, "images/" + img_name)
            img_concat_names += ";" + img_name
            i += 1

        print("images: ", img_concat_names)

        estate_info = driver.find_element(By.XPATH, "/html/body").text

        # create the Apartment object, which prepares data for
        # inserting into the database
        estate = estates.Apartment(raw_data=estate_info)

        time.sleep(5)

        counter += 1


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

    driver.close()



