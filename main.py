import json
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from config import *

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(options=options)

# SCROLL_DOWN = False
# # scroll down to bottom for loading more products (max 60-80 products) almost page 4-5
# # html is for scrolling down to bottom
# if SCROLL_DOWN:
#     html = driver.find_element(By.TAG_NAME, 'html')
#     for product in range(0, 20):
#         html.send_keys(Keys.PAGE_DOWN)
#         sleep(1)
# create a new empty json file for the products
dict_data = {'products': []}  # dictionary for data
with open('products.json', 'w') as file:
    json.dump(dict_data, file, indent=4, ensure_ascii=False)

# get all products in 100 page of website
product_counter = 0  # counter for product 1 to n in all page
for page in range(1, 5):
    page_link = f'?page={page}'
    driver.get(URL + page_link)
    print(f'Scraping page {URL}{page_link}')
    all_product = driver.find_elements(By.XPATH,
                                       value='//*[@id="plpLayoutContainer"]/section[1]/div[2]/div[1]/div/div/a')
    item_counter = 0  # counter for product 1-20 in any page that we are in
    for product in all_product:
        product_counter += 1
        item_counter += 1
        title = product.find_element(By.TAG_NAME, 'h2').text
        # I use counter for get the price of the product because
        # I can`t get the price of the product with the xpath of the "all_product"
        price = driver.find_element(By.XPATH,
                                    f'//*[@id="plpLayoutContainer"]/section[1]/div[2]/div[1]/div/div[{item_counter}]'
                                    f'/a/article/div/div/div[4]/div[1]').text
        link = product.get_attribute('href')

        # save on dictionary and json file
        dict_product_detail = {'Number': product_counter, 'title': title, 'price': price, 'link': link}
        convert_to_json(dict_product_detail)

    print(f'Scraping page {URL}{page_link} is DONE !')
    # dict_data['products'] = []

driver.quit()

# todo:add sqlite database for products
