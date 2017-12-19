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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
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
# enter into database
cursor.execute('insert into tSportys (itemName, itemNumber, itemPrice) values ("' + name + '", "' + number + '", "' + price + '");')
connection.commit()


# ------------------------------------------Aircraft Spruce Prices-------------------------------------------------



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


# close browser
driver.quit()

connection.commit()
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
cursor.execute('select * from tSportys;')
data = cursor.fetchall()
for row in data:
    product_name = row[1]
    product_number = str(row[2])
    product_price = str(row[3])
    file.write('\n    <tr>')
    file.write('\n        <td>' + str(product_name) + '</td>')
    file.write('\n        <td>' + str(product_number) + '</td>')
    file.write('\n        <td>' + str(product_price) + '</td>')
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
