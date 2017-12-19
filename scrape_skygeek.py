from selenium import webdriver
import pymysql
import time
# connection to mysql
connection = pymysql.connect(host='localhost',
                                  user='root',
                                  password='admin',
                                  db='Products')
# cursor used to exec queries
cursor = connection.cursor()
# open chrome
driver = webdriver.Chrome()


# ----------------------------------------Sky Geek---------------------------------- #
cursor.execute('delete from tSkyGeek;')


# H10-13.4
driver.get('http://www.skygeek.com/david-clark-h10-13-4.html')
time.sleep(2)
driver.find_element_by_css_selector('#orderForm > table > tbody > tr:nth-child(4) > td > img').click()
time.sleep(4)
price = driver.find_element_by_css_selector('#uw-top-right > div.item-price').text
url = "http://www.skygeek.com/david-clark-h10-13-4.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# H10-13S
driver.get('http://www.skygeek.com/h1013s.html')
time.sleep(2)
driver.find_element_by_css_selector('#orderForm > table > tbody > tr:nth-child(4) > td > img').click()
time.sleep(2)
price = driver.find_element_by_css_selector('#uw-top-right > div.item-price').text
url = "http://www.skygeek.com/h1013s.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ASA Airclassics HS-1A
driver.get('http://www.skygeek.com/asa-hs-1a.html')
time.sleep(2)
price = driver.find_element_by_css_selector('#orderForm > div > font').text
url = "http://www.skygeek.com/asa-hs-1a.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 750L
driver.get('http://www.skygeek.com/yaesu-fta-750l-handheld-vhf-transceiver-gps.html')
time.sleep(2)
price = driver.find_element_by_css_selector('#orderForm > div > font').text
url = "http://www.skygeek.com/yaesu-fta-750l-handheld-vhf-transceiver-gps.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550L
driver.get('http://www.skygeek.com/yaesu-fta-550l-handheld-vhf-transceiver.html')
time.sleep(2)
price = 'Unavailable'
url = "http://www.skygeek.com/yaesu-fta-550l-handheld-vhf-transceiver.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550AA
driver.get('http://www.skygeek.com/yaesu-fta-550l-handheld-vhf-transceiver.html')
time.sleep(2)
price = 'Unavailable'
url = "http://www.skygeek.com/yaesu-fta-550l-handheld-vhf-transceiver.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ICOM IC-A14
driver.get('http://www.skygeek.com/ic-a14-vhf-air-band-transceivers.html')
time.sleep(2)
price = 'Unavailable'
url = "http://www.skygeek.com/ic-a14-vhf-air-band-transceivers.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Jeppesen Private Pilot
driver.get('http://www.skygeek.com/js314500.html')
time.sleep(2)
price = driver.find_element_by_css_selector('#orderForm > div > font').text
url = "http://www.skygeek.com/js314500.html"
cursor.execute('insert into tSkyGeek (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


#
