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


def remove_spaces(string):
    return string.replace(" ", "")

# TODO: crate a class for parsing the data in a saparate file


root_url = "https://www.sreality.cz/"

url_apartment = root_url + "/hledani/prodej/byty"
url_house = root_url + "/hledani/domy"

driver = webdriver.Chrome()

driver.get(url_apartment)

# get links to all the apartments on a page
elements = driver.find_elements(By.TAG_NAME, "a")
links_apartments = []
for x in elements:
    href = x.get_attribute('href')
    if href is not None:
        links_apartments.append(href)

# calculate number of pages
apartments_lst_info = driver.find_element(By.XPATH, "/html/body").text
n_per_page = 20
n_total = re.search(r'Zobrazujeme výsledky 1–20 z celkem (.*?) nalezených', apartments_lst_info).group(1)
n_total = int(remove_spaces(n_total))
n_pages = floor(n_total / n_per_page)

# print("number of pages" + str(n_pages))

for i in range(0, n_pages):

    apartment_links = list(filter(lambda link: "detail/prodej/byt/" in link, links_apartments))
    apartment_link1 = apartment_links[0]

    driver.get(apartment_link1)

    # gets all the text from the page of details of a single real estate
    apartment_info = driver.find_element(By.XPATH, "/html/body").text
    # print(apartment_info)






