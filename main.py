from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from config import *

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(options=options)
driver.get(URL)
source = driver.page_source
SCROLL_DOWN=True
# scroll down to bottom for loading more products (max 60-80 products) almost page 4-5
# html is for scrolling down to bottom
if SCROLL_DOWN:
    html = driver.find_element(By.TAG_NAME, 'html')
    for product in range(0, 20):
        html.send_keys(Keys.PAGE_DOWN)
        sleep(1)
all_product = driver.find_elements(By.XPATH, value='//*[@id="plpLayoutContainer"]/section[1]/div[2]/div[1]/div/div/a')

# how count of all products in the page
print(len(all_product))
print(100 * '-')

counter = 0  # counter for product
for product in all_product:
    counter += 1
    title = product.find_element(By.TAG_NAME, 'h2').text
    # I use counter for get the price of the product because
    # I can`t get the price of the product with the xpath of the "all_product"
    price = driver.find_element(By.XPATH,
                                f'//*[@id="plpLayoutContainer"]/section[1]/div[2]/div[1]/div/div[{counter}]/a/article/div/div/div[4]/div[1]').text
    link = product.get_attribute('href')

    print(title, '\n', price, '\n', link)
    print(100 * '-')

driver.quit()
