import time
from selenium import webdriver
import pymysql

# connection to mysql
connection = pymysql.connect(host='localhost',
                                  user='root',
                                  password='admin',
                                  db='Products')
# cursor used to exec queries
cursor = connection.cursor()

# get product info for h10-13.4
browser = webdriver.Chrome()
print('Opened Chrome')

time.sleep(5)
browser.get("http://www.sportys.com/pilotshop/asa-airclassics-hs-1a-headset.html")
print('Navigated to ASA AirClassics HS-1A product page')

time.sleep(5)
browser.find_element_by_xpath("//*[contains(@id, 'x-mark')]").click()
print('Closed pop-up')

time.sleep(5)
name = browser.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
print('Name Collected')

time.sleep(5)
price = browser.find_element_by_xpath("//*[contains(@id, 'product-price-14704')]").text
print('Price collected')

print(name + '\n' + price)


