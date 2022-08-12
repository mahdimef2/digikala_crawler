import json
from datetime import datetime
from time import sleep
import sys
from config import *
import requests

create_empty_json_file()

print('start crawling -- Start time: ' + str(datetime.now()))

URL = str(sys.argv[1])  # get URL without page number in link from user
MAX_PAGE_CRAWL = int(sys.argv[2])  # get number of page that user want to crawle
category = URL.split('/', )[4][9:]
URL = f'https://api.digikala.com/v1/categories/{category}/search/'
BASE_url = "https://www.digikala.com"
product_counter = 0
for page in range(1, MAX_PAGE_CRAWL + 1):
    page_url = f'?page={page}'
    print(URL + page_url)
    data = requests.get(URL + page_url).json()['data']['products']
    print(len(data))
    for i in range(0, len(data)):
        product_counter += 1
        title_fa = data[i]['title_fa']
        title_en = data[i]['title_en']
        url = BASE_url + data[i]['url']['uri']
        price = data[i]['default_variant']['price']['selling_price']
        img_link = data[i]['images']['main']['url']
        product_id = data[i]['id']
        # print(f'#{title_fa}#)')
        # print(f' {title_en} #{url} #{price}')

        dict_product_detail = {'Number': product_counter,
                               'title_fa': title_fa,
                               'title_en': title_en,
                               'price': price,
                               'product_link': url,
                               'img_link': img_link,
                               'product_id': product_id}
        # save on json file
        convert_to_json(dict_product_detail)

    print(f'Scraping page{page} is DONE !')
