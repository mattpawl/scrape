
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

