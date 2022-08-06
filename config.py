import json

BASE_URL = "https://www.digikala.com/search/"
CATEGORY_URL = "category-mobile-phone/product-list/"
URL = BASE_URL + CATEGORY_URL


# utils functions for scraping data from the site
def convert_to_json(dict_data):
    with open('products.json') as file_open:
        main_file = json.load(file_open)
        main_file['products'].append(dict_data)
        with open('products.json', 'w') as file_write:
            json.dump(main_file, file_write, indent=4, ensure_ascii=False)
