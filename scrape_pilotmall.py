import pymysql
import time
from selenium import webdriver
import re
# connection to mysql
connection = pymysql.connect(host='localhost',
                                  user='root',
                                  password='admin',
                                  db='Products')
# cursor used to exec queries
cursor = connection.cursor()
# open chrome
driver = webdriver.Chrome()

# -------------------------------------------------Pilot Mall--------------------------------------------------- #
# clear table
cursor.execute('delete from tPilotMall')

# David Clark H10-13.4
driver.get('https://www.pilotmall.com/product/David-Clark-H10-13-4-Headset/Shop-By-Manufacturer-David-Clark')
time.sleep(2)
driver.find_element_by_css_selector('.product-page-btn-crt').click()
time.sleep(1)
price = driver.find_element_by_css_selector('table.table-design.m-b-20 > tbody > tr:nth-child(2) > td:nth-child(3)').text
url = "https://www.pilotmall.com/product/David-Clark-H10-13-4-Headset/Shop-By-Manufacturer-David-Clark"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# David Clark H10-13S
driver.get('https://www.pilotmall.com/product/David-Clark-H10-13S-Stereo-Headset/Shop-By-Manufacturer-David-Clark')
time.sleep(2)
driver.find_element_by_css_selector('.product-page-btn-crt').click()
time.sleep(1)
price = driver.find_element_by_css_selector('#SubpageMainContainer > section > div > div > div:nth-child(2) > div:nth-child(2) > form > table > tbody > tr:nth-child(3) > td:nth-child(3)').text
url = "https://www.pilotmall.com/product/David-Clark-H10-13S-Stereo-Headset/Shop-By-Manufacturer-David-Clark"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ASA AirClassics HS-1A
driver.get('https://www.pilotmall.com/product/ASA-AirClassics-Headset-/Shop-By-Manufacturer-ASA-Publications')
time.sleep(2)
driver.find_element_by_css_selector('.product-page-btn-crt').click()
time.sleep(1)
price = driver.find_element_by_css_selector('#SubpageMainContainer > section > div > div > div:nth-child(2) > div:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(3)').text
url = "https://www.pilotmall.com/product/ASA-AirClassics-Headset-/Shop-By-Manufacturer-ASA-Publications"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA 750L
driver.get('https://www.pilotmall.com/product/Yaesu-FTA-750L-Handheld-VHF-Transceiver-w-GPS/transceivers')
time.sleep(2)
price = driver.find_element_by_css_selector('#HomeContent > section > div > div:nth-child(3) > div.Clear.PaddingTop15 > div.product-image-details > form > div.product-page-price-quantity-cart-wish > div.product-page-price > span:nth-child(4)').text
url = "https://www.pilotmall.com/product/Yaesu-FTA-750L-Handheld-VHF-Transceiver-w-GPS/transceivers"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA 550L
driver.get('https://www.pilotmall.com/product/Yaesu-FTA-550L-Li-Ion-Handheld-VHF-Transceiver/transceivers')
time.sleep(2)
price = driver.find_element_by_css_selector('#HomeContent > section > div > div:nth-child(3) > div.Clear.PaddingTop15 > div.product-image-details > form > div.product-page-price-quantity-cart-wish > div.product-page-price > span:nth-child(4)').text
url = "https://www.pilotmall.com/product/Yaesu-FTA-550L-Li-Ion-Handheld-VHF-Transceiver/transceivers"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA 550AA
driver.get('https://www.pilotmall.com/product/Yaesu-FTA-550-AA-Handheld-VHF-Transceiver/transceivers')
time.sleep(2)
price = driver.find_element_by_css_selector('#HomeContent > section > div > div:nth-child(3) > div.Clear.PaddingTop15 > div.product-image-details > form > div.product-page-price-quantity-cart-wish > div.product-page-price > span:nth-child(4)').text
url = "https://www.pilotmall.com/product/Yaesu-FTA-550-AA-Handheld-VHF-Transceiver/transceivers"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# The following are placeholders, the supplier doesn't sell the following but something has to occupy the database table


# ICOM IC-A14
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()

# Jeppesen Private Pilot
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Aeroshell W100 Plus
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W15W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W100 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W80 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# 100 Mineral Oil
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Phillips 66 SAE20W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()
