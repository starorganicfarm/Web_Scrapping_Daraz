import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)


@app.route('/scrape/<string:product>')
def scrape(product):
    # open the browser
    browser = webdriver.Chrome()
    # Create Chrome WebDriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)

    if product == "Nestle Pure Life 5L":
        product = "PURELIFE 5L"
    elif product == "Lays Yogurt and Herb Rs.60":
        product = "Lays Yogurt and Herb Rs.60 345"
    elif product == "Sting 500ml Energy Drink":
        product = "344706245_PK-1769604675"
    elif product == "Mountain Dew Drink 500ml":
        product = "412591006_PK-1970017737"

    # load the webpage
    browser.get(f'https://www.daraz.pk/catalog/?q={product}')

    titles = browser.find_elements(By.CLASS_NAME, 'title--wFj93')
    prices = browser.find_elements(By.CLASS_NAME, 'price--NVB62')

    result_list = []

    for title, price in zip(titles, prices):
        title_text = title.text
        price_text = price.text

        # Remove all non-digit characters except decimal point
        price_value = re.sub(r'[^\d.]', '', price_text)
        price_value = price_value.replace('.', '')
        price_value = int(price_value)

        if product == 'Lays Yogurt and Herb Rs.60 345' and ("Lays Yogurt and Herb" in title_text) and (
                55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'PURELIFE 5L' and (215 <= price_value <= 235):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Pepsi 500ml Bottle' and ("Pepsi" in title_text) and (130 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Kurkure Chatni Chaska 20' and ("Kurkure Chatni" in title_text) and (
                10 <= float(price_value) <= 20):
            result_list.append({
                'title': product,
                'price': 20
            })
        elif product == '344706245_PK-1769604675' and ("Sting" in title_text) and (130 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays Masala Rs.60' and ("Lays Masala" in title_text) and (55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays French Cheese Rs.60' and ("Lays French Cheese" in title_text) and (
                55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == '412591006_PK-1970017737' and ("Mountain Dew" in title_text) and (120 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays French Cheese 14 g':
            result_list.append({
                'title': product,
                'price': 20
            })
            break
        elif product == 'Lays Masala 14':
            result_list.append({
                'title': product,
                'price': 20
            })
            break
        elif product == 'Lays Salt 14':
            result_list.append({
                'title': product,
                'price': 20
            })
            break
        elif product == 'Lays Wavy BBQ Rs.30':
            result_list.append({
                'title': product,
                'price': 30
            })
            break
        elif product == 'Milo 180 ml':
            result_list.append({
                'title': product,
                'price': 80
            })
            break
        elif product == 'Olpers Badam Zafran':
            result_list.append({
                'title': product,
                'price': 75
            })
            break
        elif product == 'Gluco Biscuit':
            result_list.append({
                'title': product,
                'price': 40
            })
            break
        elif product == 'Slice Juice 200ml Mango':
            result_list.append({
                'title': product,
                'price': 38
            })
            break
        elif product == 'Lays Paprika Rs.30':
            result_list.append({
                'title': product,
                'price': 30
            })
            break

    time.sleep(2)
    browser.close()

    # return the results as JSON
    return jsonify(results=result_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)


@app.route('/scrape/<string:product>')
def scrape(product):
    # open the browser
    browser = webdriver.Chrome()
    # Create Chrome WebDriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)

    if product == "Nestle Pure Life 5L":
        product = "PURELIFE 5L"
    elif product == "Lays Yogurt and Herb Rs.60":
        product = "Lays Yogurt and Herb Rs.60 345"
    elif product == "Sting 500ml Energy Drink":
        product = "344706245_PK-1769604675"
    elif product == "Mountain Dew Drink 500ml":
        product = "412591006_PK-1970017737"

    # load the webpage
    browser.get(f'https://www.daraz.pk/catalog/?q={product}')

    titles = browser.find_elements(By.CLASS_NAME, 'title--wFj93')
    prices = browser.find_elements(By.CLASS_NAME, 'price--NVB62')

    result_list = []

    for title, price in zip(titles, prices):
        title_text = title.text
        price_text = price.text

        # Remove all non-digit characters except decimal point
        price_value = re.sub(r'[^\d.]', '', price_text)
        price_value = price_value.replace('.', '')
        price_value = int(price_value)

        if product == 'Lays Yogurt and Herb Rs.60 345' and ("Lays Yogurt and Herb" in title_text) and (
                55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'PURELIFE 5L' and (215 <= price_value <= 235):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Pepsi 500ml Bottle' and ("Pepsi" in title_text) and (130 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Kurkure Chatni Chaska 20' and ("Kurkure Chatni" in title_text) and (
                10 <= float(price_value) <= 20):
            result_list.append({
                'title': product,
                'price': 20
            })
        elif product == '344706245_PK-1769604675' and ("Sting" in title_text) and (130 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays Masala Rs.60' and ("Lays Masala" in title_text) and (55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays French Cheese Rs.60' and ("Lays French Cheese" in title_text) and (
                55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == '412591006_PK-1970017737' and ("Mountain Dew" in title_text) and (120 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays French Cheese 14 g':
            result_list.append({
                'title': product,
                'price': 20
            })
            break
        elif product == 'Lays Masala 14':
            result_list.append({
                'title': product,
                'price': 20
            })
            break
        elif product == 'Lays Salt 14':
            result_list.append({
                'title': product,
                'price': 20
            })
            break
        elif product == 'Lays Wavy BBQ Rs.30':
            result_list.append({
                'title': product,
                'price': 30
            })
            break
        elif product == 'Milo 180 ml':
            result_list.append({
                'title': product,
                'price': 80
            })
            break
        elif product == 'Olpers Badam Zafran':
            result_list.append({
                'title': product,
                'price': 75
            })
            break
        elif product == 'Gluco Biscuit':
            result_list.append({
                'title': product,
                'price': 40
            })
            break
        elif product == 'Slice Juice 200ml Mango':
            result_list.append({
                'title': product,
                'price': 38
            })
            break
        elif product == 'Lays Paprika Rs.30':
            result_list.append({
                'title': product,
                'price': 30
            })
            break

    time.sleep(2)
    browser.close()

    # return the results as JSON
    return jsonify(results=result_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
