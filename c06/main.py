import random
import string
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.by import By

xPaths = {
    'cookies': "//div[@class='ok closeButton']",
    'en': "//a[@href='http://www.pap.pl/en']",
    'business': "//a[@href='/en/business']",
    'lastPage': "//a[@title='Go to last page']"
}

driver = webdriver.Chrome()
driver.get('https://www.pap.pl/')

print('Accept cookies')
driver.find_element(by=By.XPATH, value=xPaths['cookies']).click()

print('Enlarge the browser window to full screen')
driver.maximize_window()

print('Change the website language to English')
driver.find_element(by=By.XPATH, value=xPaths['en']).click()

print('Enter the Business section')
driver.find_element(by=By.XPATH, value=xPaths['business']).click()

print('From the business section download all titles to the titles list')
titlesList = driver\
    .find_elements(
        by=By.CSS_SELECTOR,
        value='div.newsList div div.textWrapper h1 a, div.newsList div div.row ul li div.textWrapper h2 a'
    )

for el in titlesList:
    print(el.text)

print('Download all photos from this section to your local drive')
paths = driver.\
    find_elements(
        by=By.CSS_SELECTOR,
        value='div.newsList div div.imageWrapper a img, div.newsList div div.row ul li div.imageWrapper a img'
    )

for path in paths:
    name = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(15))
    urlretrieve(path.get_attribute("src"), f"{name}.jpg")

print('Scroll down the page')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

print('Go to the last page and prints its number (text attribute)')
lastPage = driver.find_element(by=By.XPATH, value=xPaths['lastPage'])
lastPage.click()
print(driver.current_url.split("=")[1])

driver.quit()
