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
# clear table before running
cursor.execute('delete from tAircraftSpruce;')
# open chrome
driver = webdriver.Chrome()

# David Clark H10-13.4
driver.get('http://www.aircraftspruce.com/catalog/avpages/h10_134.php')
time.sleep(2)
driver.find_element_by_id('product_addtocart').click()
time.sleep(2)
price = driver.find_element_by_id('price-11-03815').text
url = "http://www.aircraftspruce.com/catalog/avpages/h10_134.php"
print(price)
# enter into database
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# David Clark H10-13S
driver.get('http://www.aircraftspruce.com/catalog/avpages/h10_13S.php')
time.sleep(2)
driver.find_element_by_id('product_addtocart').click()
time.sleep(2)
price = driver.find_element_by_id('price-11-03816').text
url = "http://www.aircraftspruce.com/catalog/avpages/h10_13S.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ASA Airclassics HS-1A
driver.get('http://www.aircraftspruce.com/catalog/avpages/asaheadsetclassics.php')
time.sleep(2)
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/avpages/asaheadsetclassics.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 750L
driver.get('http://www.aircraftspruce.com/catalog/avpages/yaesuVertexFTA750L.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddA']/option[text()='110v']").click()
time.sleep(1)
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/avpages/yaesuVertexFTA750L.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550L
driver.get('http://www.aircraftspruce.com/catalog/avpages/yaesuVertex550L.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddA']/option[text()='110 V']").click()
time.sleep(1)
price = driver.find_element_by_class_name('product_price').text
url = 'http://www.aircraftspruce.com/catalog/avpages/yaesuVertex550L.php'
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550AA
driver.get('http://www.aircraftspruce.com/catalog/avpages/yaesuVertex11-12461.php')
time.sleep(2)
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/avpages/yaesuVertex11-12461.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()

# ICOM IC-A14
driver.get('http://www.aircraftspruce.com/catalog/avpages/icomA14full_110.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddA']/option[text()='with 110V Charger']").click()
time.sleep(1)
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/avpages/icomA14full_110.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Jeppesen Private Pilot
driver.get('http://www.aircraftspruce.com/catalog/bvpages/gfdprivpilotman.php')
time.sleep(2)
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/bvpages/gfdprivpilotman.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Aeroshell W100 Plus
driver.get('http://www.aircraftspruce.com/catalog/eppages/aeroshelloils3.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddO']/option[text()='Case of 12']").click()
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/eppages/aeroshelloils3.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()



# Aeroshell 15W-50
driver.get('http://www.aircraftspruce.com/catalog/eppages/aeroshelloils2.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddO']/option[text()='Case of 12 Quarts']").click()
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/eppages/aeroshelloils2.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Aeroshell W100 SAE50
driver.get('http://www.aircraftspruce.com/catalog/eppages/aeroshelloils.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddO']/option[text()='Case of 12']").click()
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/eppages/aeroshelloils.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Aeroshell SAE W80
driver.get('http://www.aircraftspruce.com/catalog/eppages/aeroshelloils4.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddO']/option[text()='Case of 12']").click()
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/eppages/aeroshelloils4.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# AeroShell 100 Mineral Aviation Oil
driver.get('http://www.aircraftspruce.com/catalog/eppages/aeroshelloils6.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='ddO']/option[text()='Case of 12']").click()
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/eppages/aeroshelloils6.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Phillips 20W50
driver.get('http://www.aircraftspruce.com/catalog/eppages/phillipsxc.php')
time.sleep(2)
driver.find_element_by_xpath("//select[@name='dda']/option[text()='Case of 12 Quarts']").click()
price = driver.find_element_by_class_name('product_price').text
url = "http://www.aircraftspruce.com/catalog/eppages/phillipsxc.php"
cursor.execute('insert into tAircraftSpruce (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


driver.close()
