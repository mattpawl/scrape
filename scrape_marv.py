import pymysql
import time
from selenium import webdriver
# connection to mysql
connection = pymysql.connect(host='localhost',
                                  user='root',
                                  password='admin',
                                  db='Products')
# cursor used to exec queries
cursor = connection.cursor()
# clear table before running
cursor.execute('delete from tMarvGolden;')
# open chrome
driver = webdriver.Chrome()


# -------------------------------------------------Marv Golden------------------------------------------------------- #


# David Clark H10-13.4

driver.get('http://www.marvgolden.com/david-clark-h10-13-4-headset.html')
time.sleep(2)
driver.find_element_by_id('product-price-796').click()
time.sleep(1)
price = driver.find_element_by_css_selector('.regular-price .price').text
url = "http://www.marvgolden.com/david-clark-h10-13-4-headset.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# David Clark H10-13S
driver.get('http://www.marvgolden.com/david-clark-h10-13s-headset.html')
time.sleep(2)
driver.find_element_by_id('product-price-802').click()
time.sleep(1)
price = driver.find_element_by_css_selector('.regular-price .price').text
url = "http://www.marvgolden.com/david-clark-h10-13s-headset.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ASA Airclassics HS-1A
driver.get('http://www.marvgolden.com/asa-airclassics-hs-1a-headset.html')
time.sleep(2)
price = driver.find_element_by_css_selector('.regular-price .price').text
url = "http://www.marvgolden.com/asa-airclassics-hs-1a-headset.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 750L
driver.get('http://www.marvgolden.com/yaesu-fta-750l-nav-com-gps-aviation-transceiver-u-s-110-volt.html')
time.sleep(2)
price = driver.find_element_by_id('product-price-7676').text
url = "http://www.marvgolden.com/yaesu-fta-750l-nav-com-gps-aviation-transceiver-u-s-110-volt.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550L
driver.get('http://www.marvgolden.com/yaesu-fta-550l-nav-com-aviation-transceiver-u-s-110-volt.html')
time.sleep(2)
price = driver.find_element_by_id('product-price-7674').text
url = "http://www.marvgolden.com/yaesu-fta-550l-nav-com-aviation-transceiver-u-s-110-volt.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550AA
driver.get('http://www.marvgolden.com/yaesu-fta-550-aa-nav-com-aviation-transceiver.html')
time.sleep(2)
price = driver.find_element_by_id('product-price-7669').text
url = "http://www.marvgolden.com/yaesu-fta-550-aa-nav-com-aviation-transceiver.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ICOM IC-A14
driver.get('http://www.marvgolden.com/icom-ic-a14-transceiver-u-s-110-volt.html')
time.sleep(2)
price = driver.find_element_by_css_selector('.regular-price .price').text
url = "http://www.marvgolden.com/icom-ic-a14-transceiver-u-s-110-volt.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Jeppesen Private Pilot
driver.get('http://www.marvgolden.com/jeppesen-gfd-private-pilot-manual.html')
time.sleep(2)
price = driver.find_element_by_css_selector('.regular-price .price').text
url = "http://www.marvgolden.com/jeppesen-gfd-private-pilot-manual.html"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


driver.close()
