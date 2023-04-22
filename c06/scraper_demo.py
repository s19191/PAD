from string import printable
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://uk.shop.allpressespresso.com/')

driver.maximize_window() # zwiekszamy wielkosc okna

time.sleep(1)

cookies = driver.find_element_by_xpath('//*[@id="ccc-notify-accept"]')
cookies.click()

descriptions = []

description = driver.find_element_by_xpath('//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[1]/div/div/form/div[2]/p').text
description2 = driver.find_element_by_xpath('//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[2]/div/div/form/div[2]/p').text
descriptions.append(description)
descriptions.append(description2)
print(descriptions)


driver.quit()


class Scraper():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_desxriptions(self):
        descriptions = []
        description = driver.find_element_by_xpath('//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[1]/div/div/form/div[2]/p').text
        description2 = driver.find_element_by_xpath('//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[2]/div/div/form/div[2]/p').text
        descriptions.append(description)
        descriptions.append(description2)
        return descriptions
