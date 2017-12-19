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
price = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_lblPriceValue > span')
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



