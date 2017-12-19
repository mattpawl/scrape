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
cursor.execute('delete from tSportys;')
# open chrome
driver = webdriver.Chrome()
# --------------------------------------------SPORTY'S PRICES---------------------------------------------------------#


# David Clark H10-13.4
driver.get("http://www.sportys.com/pilotshop/david-clark-h10-13-4-headset.html")
time.sleep(2)
# close popup
driver.find_element_by_xpath("//*[contains(@id, 'x-mark')]").click()
# open price box
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@id, 'msrp-popup')]").click()
# get name and price from info box
name = driver.find_element_by_xpath("//*[contains(@id, 'map-popup-heading')]").text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_id('map-popup-price').text
url = "http://www.sportys.com/pilotshop/david-clark-h10-13-4-headset.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()

# David Clark H10-13S
driver.get("http://www.sportys.com/pilotshop/david-clark-h10-13s-headset-stereo.html")
time.sleep(2)
# open price box
driver.find_element_by_xpath("//*[contains(@id, 'msrp-popup')]").click()
# get name and price from info box
name = driver.find_element_by_xpath("//*[contains(@id, 'map-popup-heading')]").text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_id('map-popup-price').text
url = "http://www.sportys.com/pilotshop/david-clark-h10-13s-headset-stereo.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# ASA Airclassics HS-1A
driver.get('http://www.sportys.com/pilotshop/aviation-headsets/asa-headset-and-accessories/asa-airclassics-hs-1a-headset.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-14704')]").text
url = "http://www.sportys.com/pilotshop/aviation-headsets/asa-headset-and-accessories/asa-airclassics-hs-1a-headset.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA-750L
driver.get('http://www.sportys.com/pilotshop/yaesu-fta-750l-airband-transceiver.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-5463')]").text
url = "http://www.sportys.com/pilotshop/yaesu-fta-750l-airband-transceiver.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA-550L
driver.get('http://www.sportys.com/pilotshop/yaesu-fta-550l-pro-x-airband-transceiver.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-5464')]").text
url = "http://www.sportys.com/pilotshop/yaesu-fta-550l-pro-x-airband-transceiver.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550AA
driver.get('http://www.sportys.com/pilotshop/yaesu-fta-550aa-airband-transceiver.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-5465')]").text
url = "http://www.sportys.com/pilotshop/yaesu-fta-550aa-airband-transceiver.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# ICOM IC-A14
driver.get('http://www.sportys.com/pilotshop/icom-ic-a14-com-transceiver.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-3462')]").text
url = "http://www.sportys.com/pilotshop/icom-ic-a14-com-transceiver.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# Jeppesen Private Pilot Manual
driver.get('http://www.sportys.com/pilotshop/private-pilot-jeppesen.html?___SID=U')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-3154')]").text
url = "http://www.sportys.com/pilotshop/private-pilot-jeppesen.html?___SID=U"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# Aeroshell W100 Plus Aviation Oil
driver.get('http://www.sportys.com/pilotshop/aeroshell-100w-plus-aviation-oil.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-4672')]").text
url = "http://www.sportys.com/pilotshop/aeroshell-100w-plus-aviation-oil.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# 15W50 Aviation Oil Case
driver.get('http://www.sportys.com/pilotshop/15w50-aviation-oil-case.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-4245')]").text
url = "http://www.sportys.com/pilotshop/15w50-aviation-oil-case.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# W100 SAE Aviation Oil Case
driver.get('http://www.sportys.com/pilotshop/w100-sae-aviation-oil-case.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-4246')]").text
url = "http://www.sportys.com/pilotshop/w100-sae-aviation-oil-case.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# W80 Aviation Oil Case
driver.get('http://www.sportys.com/pilotshop/w80-sae-aviation-oil-case.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-4247')]").text
url = "http://www.sportys.com/pilotshop/w80-sae-aviation-oil-case.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# Aeroshell 100 Mineral Aviation Oil
driver.get('http://www.sportys.com/pilotshop/aeroshell-100-mineral-aviation-oil.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-4673')]").text
url = "http://www.sportys.com/pilotshop/aeroshell-100-mineral-aviation-oil.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()


# Phillips 66 20W50
driver.get('http://www.sportys.com/pilotshop/phillips-66-x-c-aviation-oil-sae20w-50-case-of-12-quarts.html')
time.sleep(2)
# get name and price
name = driver.find_element_by_css_selector('.product-view .product-essential .product-essential-info-container .product-essential-basics .product-shop .product-name h1').text
number = driver.find_element_by_class_name('sku').text
number = number[-6:]
number = number.replace(" ", "")
price = driver.find_element_by_xpath("//*[contains(@id, 'product-price-17979')]").text
url = "http://www.sportys.com/pilotshop/phillips-66-x-c-aviation-oil-sae20w-50-case-of-12-quarts.html"
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice, itemURL) values ("' + name + '", "' + number + '", "' + price + '", "' + url + '");')
connection.commit()



# ------------------------------------------Aircraft Spruce Prices-------------------------------------------------

# clear prices before running
cursor.execute('delete from tAircraftSpruce')


# David Clark H10-13.4
driver.get('http://www.aircraftspruce.com/catalog/avpages/h10_134.php')
time.sleep(2)
driver.find_element_by_id('product_addtocart').click()
time.sleep(2)
price = driver.find_element_by_id('price-11-03815').text
url = "http://www.aircraftspruce.com/catalog/avpages/h10_134.php"
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


# -------------------------------------------------Marv Golden----------------------------------------------------$
cursor.execute('delete from tMarvGolden;')

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


# The rest of these are placeholders that say marv golden doesn't carry a certain product


# Aeroshell W100 Plus
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()
# W15W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()
# W100 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()
# W80 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()
# 100 Mineral Oil
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()
# Phillips 66 SAE20W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tMarvGolden (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


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
selector = '#HomeContent > section > div > div:nth-child(3) > div.Clear.PaddingTop15 > div.product-image-details > form > div.product-page-price-quantity-cart-wish > div.product-page-price > span:nth-child(4)'
price = driver.find_element_by_css_selector(selector).text
url = "https://www.pilotmall.com/product/Yaesu-FTA-750L-Handheld-VHF-Transceiver-w-GPS/transceivers"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA 550L
driver.get('https://www.pilotmall.com/product/Yaesu-FTA-550L-Li-Ion-Handheld-VHF-Transceiver/transceivers')
time.sleep(2)
selector = '#HomeContent > section > div > div:nth-child(3) > div.Clear.PaddingTop15 > div.product-image-details > form > div.product-page-price-quantity-cart-wish > div.product-page-price > span:nth-child(4)'
price = driver.find_element_by_css_selector(selector).text
url = "https://www.pilotmall.com/product/Yaesu-FTA-550L-Li-Ion-Handheld-VHF-Transceiver/transceivers"
cursor.execute('insert into tPilotMall (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA 550AA
driver.get('https://www.pilotmall.com/product/Yaesu-FTA-550-AA-Handheld-VHF-Transceiver/transceivers')
time.sleep(2)
selector = '#HomeContent > section > div > div:nth-child(3) > div.Clear.PaddingTop15 > div.product-image-details > form > div.product-page-price-quantity-cart-wish > div.product-page-price > span:nth-child(4)'
price = driver.find_element_by_css_selector(selector).text
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


# ------------------------------------------------Gulf Coast Prices---------------------------------------------- #


# clear table
cursor.execute('delete from tGulfCoast')

# H10 -13.4
driver.get('https://www.gulfcoastavionics.com/products/300-david-clark-h10-13.4-headset.aspx')
time.sleep(2)
driver.find_element_by_id('btnAddToCart').click()
time.sleep(1)
price = driver.find_element_by_css_selector('#frm > div > table > tbody > tr:nth-child(2) > td.td-price').text
url = "https://www.gulfcoastavionics.com/products/300-david-clark-h10-13.4-headset.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# H10 - 13S
driver.get('https://www.gulfcoastavionics.com/products/301-david-clark-h10-13s-headset.aspx')
time.sleep(2)
driver.find_element_by_id('btnAddToCart').click()
time.sleep(1)
price = driver.find_element_by_css_selector('#frm > div > table > tbody > tr:nth-child(2) > td.td-price').text
url = "https://www.gulfcoastavionics.com/products/301-david-clark-h10-13s-headset.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ASA Airclassics HS-1A
driver.get('https://www.gulfcoastavionics.com/products/3822-airclassics-hs-1a-headset.aspx')
time.sleep(2)
price = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_lblPriceValue > span').text
url = "https://www.gulfcoastavionics.com/products/3822-airclassics-hs-1a-headset.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA 750L
driver.get('https://www.gulfcoastavionics.com/products/3968-fta-750l-handheld-vhf-gps.aspx')
time.sleep(2)
price = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_lblPriceValue > span').text
url = "https://www.gulfcoastavionics.com/products/3968-fta-750l-handheld-vhf-gps.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()

# Yaesu FTA-550L
driver.get('https://www.gulfcoastavionics.com/products/3967-fta-550-series-handheld-vhf.aspx')
time.sleep(2)
driver.find_element_by_xpath("//select[@id='selAttr1']/option[text()='Li-ion Version']").click()
time.sleep(1)
price = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_lblPriceValue > span').text
url = "https://www.gulfcoastavionics.com/products/3967-fta-550-series-handheld-vhf.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu FTA-550AA
driver.get('https://www.gulfcoastavionics.com/products/3967-fta-550-series-handheld-vhf.aspx')
time.sleep(2)
driver.find_element_by_xpath("//select[@id='selAttr1']/option[text()='AA Battery Version']").click()
time.sleep(1)
price = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_lblPriceValue > span').text
url = "https://www.gulfcoastavionics.com/products/3967-fta-550-series-handheld-vhf.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ICOM IC-A14
driver.get('https://www.gulfcoastavionics.com/products/1335-icom-ic-a14.aspx')
time.sleep(2)
price = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_lblPriceValue > span').text
url = "https://www.gulfcoastavionics.com/products/1335-icom-ic-a14.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Jeppesen Private Pilot
driver.get('https://www.gulfcoastavionics.com/products/642-gfd-private-pilot-textbook.aspx')
time.sleep(2)
price = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_lblPriceValue > span').text
url = "https://www.gulfcoastavionics.com/products/642-gfd-private-pilot-textbook.aspx"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# The following are placeholders, the supplier doesn't sell the following but something has to occupy the database table


# Aeroshell W100 Plus
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W15W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W100 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W80 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# 100 Mineral Oil
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Phillips 66 SAE20W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tGulfCoast (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# --------------------------------------------Amazon----------------------------------------- #
cursor.execute('delete from tAmazon;')

# H10-13.4
driver.get('https://www.amazon.com/David-Clark-H10-13-4-Aviation-Headset/dp/B0011Z9PM2/ref=sr_1_2?ie=UTF8&qid=1513614881&sr=8-2&keywords=h10-13.4')
print('connected')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/David-Clark-H10-13-4-Aviation-Headset/dp/B0011Z9PM2/ref=sr_1_2?ie=UTF8&qid=1513614881&sr=8-2&keywords=h10-13.4"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# H10-13S
driver.get('https://www.amazon.com/David-Clark-H10-13S-Stereo-Headset/dp/B002CJ3NQK/ref=sr_1_2?s=electronics&ie=UTF8&qid=1513615269&sr=1-2&keywords=h10-13s')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/David-Clark-H10-13S-Stereo-Headset/dp/B002CJ3NQK/ref=sr_1_2?s=electronics&ie=UTF8&qid=1513615269&sr=1-2&keywords=h10-13s"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ASA Airclassics HS-1A
driver.get('https://www.amazon.com/ASA-HS-1-Headset-Aviation/dp/B001THL8SQ/ref=sr_1_1?s=electronics&ie=UTF8&qid=1513615339&sr=1-1&keywords=asa+airclassics+hs-1a+headset')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/ASA-HS-1-Headset-Aviation/dp/B001THL8SQ/ref=sr_1_1?s=electronics&ie=UTF8&qid=1513615339&sr=1-1&keywords=asa+airclassics+hs-1a+headset"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 750L
driver.get('https://www.amazon.com/Yaesu-FTA750L-Handheld-VHF-Transceiver/dp/B00JFJSTJG/ref=sr_1_1?s=electronics&ie=UTF8&qid=1513615409&sr=1-1&keywords=yaesu+fta-750l')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/Yaesu-FTA750L-Handheld-VHF-Transceiver/dp/B00JFJSTJG/ref=sr_1_1?s=electronics&ie=UTF8&qid=1513615409&sr=1-1&keywords=yaesu+fta-750l"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()

# Yaesu 550L
driver.get('https://www.amazon.com/Yaesu-FTA550L-Handheld-Transceiver-Battery/dp/B00JFJUCH8/ref=sr_1_2?s=electronics&ie=UTF8&qid=1513615465&sr=1-2&keywords=yaesu+fta-550l')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/Yaesu-FTA550L-Handheld-Transceiver-Battery/dp/B00JFJUCH8/ref=sr_1_2?s=electronics&ie=UTF8&qid=1513615465&sr=1-2&keywords=yaesu+fta-550l"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Yaesu 550AA
driver.get('https://www.amazon.com/Yaesu-FTA550-Handheld-VHF-Transceiver/dp/B00JFJU5Y8/ref=sr_1_3?s=electronics&ie=UTF8&qid=1513615524&sr=1-3&keywords=yaesu+fta-550aa')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/Yaesu-FTA550-Handheld-VHF-Transceiver/dp/B00JFJU5Y8/ref=sr_1_3?s=electronics&ie=UTF8&qid=1513615524&sr=1-3&keywords=yaesu+fta-550aa"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# ICOM IC-A14
driver.get('https://www.amazon.com/Icom-IC-A14-VHF-Band-transceiver/dp/B003EN1VDK/ref=sr_1_3?s=electronics&ie=UTF8&qid=1513615591&sr=1-3&keywords=icom+ic-a14')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/Icom-IC-A14-VHF-Band-transceiver/dp/B003EN1VDK/ref=sr_1_3?s=electronics&ie=UTF8&qid=1513615591&sr=1-3&keywords=icom+ic-a14"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Jeppesen Private Pilot
driver.get('https://www.amazon.com/Jeppesen-Private-Pilot-Manual-Textbook/dp/B01K0L4BA8/ref=sr_1_4?s=electronics&ie=UTF8&qid=1513615799&sr=1-4&keywords=jeppesen+private+pilot')
time.sleep(2)
price = driver.find_element_by_id('priceblock_ourprice').text
url = "https://www.amazon.com/Jeppesen-Private-Pilot-Manual-Textbook/dp/B01K0L4BA8/ref=sr_1_4?s=electronics&ie=UTF8&qid=1513615799&sr=1-4&keywords=jeppesen+private+pilot"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# The following are placeholders, the supplier doesn't sell the following but something has to occupy the database table


# Aeroshell W100 Plus
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W15W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W100 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# W80 SAE
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# 100 Mineral Oil
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# Phillips 66 SAE20W50
price = "N/A"
url = "https://www.google.com/"
cursor.execute('insert into tAmazon (itemPrice, itemURL) values ("' + price + '", "' + url + '");')
connection.commit()


# close browser
driver.quit()


# write HTML page
file = open('/var/www/html/index.html', 'w')

file.write('<!DOCTYPE html>')
file.write('\n<html>')
file.write('\n<style>')
file.write('\nth, td {')
file.write('\npadding: 2px;')
file.write('\n}')
file.write('\n</style>')

file.write('\n<body>')
file.write('\n    <div id="top" align="center">')
file.write('\n        <h2> Sportys Competitor Prices </h2>')
file.write('\n        <h3 id="date"></h3>')
file.write('\n    </div>')
file.write('\n<table style="border-collapse: collapse; width: 80%; margin: 0px auto;" cellpadding="0" cellspacing="0" border="none" >')
file.write('\n    <tr>')
file.write('\n        <th>Item Name</th>')
file.write('\n        <th>Item Number</th>')
file.write('\n        <th>Sportys<br>www.sportys.com/pilotshop</th>')
file.write('\n        <th>Aircraft Spruce<br>www.aircraftspruce.com</th>')
file.write('\n        <th>Marv Golden<br>www.marvgolden.com</th>')
file.write('\n        <th>Pilot Mall<br>www.pilotmall.com</th>')
file.write('\n        <th>Gulf Coast<br>www.gulfcoastavionics.com</th>')
file.write('\n        <th>Amazon<br>www.amazon.com</th>')
file.write('\n        <th>Skygeek<br>www.skygeek.com</th>')
file.write('\n    </tr>')


# write data to table
cursor.execute('select * from tSportys;')
sportys_data = cursor.fetchall()
cursor.execute('select * from tAircraftSpruce;')
aircraftspruce_data = cursor.fetchall()
cursor.execute('select * from tMarvGolden;')
marvgolden_data = cursor.fetchall()
cursor.execute('select * from tPilotMall;')
pilotmall_data = cursor.fetchall()
cursor.execute('select * from tGulfCoast;')
gulfcoast_data = cursor.fetchall()
cursor.execute('select * from tAmazon;')
amazon_data = cursor.fetchall()
count = 0
for row in sportys_data:
    spruce = aircraftspruce_data[count]
    marv = marvgolden_data[count]
    mall = pilotmall_data[count]
    gulf = gulfcoast_data[count]
    amazon = amazon_data[count]
    count += 1
    file.write('\n    <tr>')
    file.write('\n        <td>' + row[1] + '</td>')
    file.write('\n        <td>' + row[2] + '</td>')
    file.write('\n        <td><a href="' + row[4] + '" target="_blank">' + row[3] + '</td>')
    file.write('\n        <td><a href="' + spruce[2] + '" target="_blank">' + spruce[1] + '</td>')
    file.write('\n        <td><a href="' + marv[2] + '" target="_blank">' + marv[1] + '</td>')
    file.write('\n        <td><a href="' + mall[2] + '" target="_blank">' + mall[1] + '</td>')
    file.write('\n        <td><a href="' + gulf[2] + '" target="_blank">' + gulf[1] + '</td>')
    file.write('\n        <td><a href="' + amazon[2] + '" target="_blank">' + amazon[1] + '</td>')
    file.write('\n        <td>Skygeek price</td>')
    file.write('\n    </tr>')
file.write('\n</body>')
file.write('\n</html>')

file.write('\n<script>')
file.write('\n    n = new Date();')
file.write('\n    y = n.getFullYear();')
file.write('\n    m = n.getMonth() + 1;')
file.write('\n    d = n.getDate();')
file.write('\n    document.getElementById("date").innerHTML = m + "/" + d + "/" + y;')
file.write('\n</script>')

file.close()

print('HTML Page Generated. View at 10.10.11.106')

