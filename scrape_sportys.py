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
browser.get("http://www.sportys.com/pilotshop/david-clark-h10-13-4-headset.html")
print('Navigated to H10-13.4 product page')

time.sleep(5)
browser.find_element_by_xpath("//*[contains(@id, 'x-mark')]").click()
print('Closed pop-up')

time.sleep(5)
browser.find_element_by_xpath("//*[contains(@id, 'msrp-popup')]").click()
print('Opened price box')

time.sleep(5)
name = browser.find_element_by_xpath("//*[contains(@id, 'map-popup-heading')]").text
print('Name collected')

time.sleep(5)
price = browser.find_element_by_id('map-popup-price').text
print('Price collected')



# isolate url
def shorten(s, subs):
    i = s.index(subs)
    return s[:i+len(subs)]
website = shorten("http://www.sportys.com/pilotshop/david-clark-h10-13-4-headset.html", '.com')

# insert scraped data into webpage

cursor.execute('insert into tProducts (productName, productSeller, productPrice) values ("' + name + '", "' + website + '", "' + price + '");')
connection.commit()
print('H10-13.4 entered into database')

# get product info for h10-13s
time.sleep(5)
browser.get("http://www.sportys.com/pilotshop/david-clark-h10-13s-headset-stereo.html")
print('Navigated to H10-13s product page')

time.sleep(5)
browser.find_element_by_xpath("//*[contains(@id, 'msrp-popup')]").click()
print('Opened price box')

time.sleep(5)
name = browser.find_element_by_xpath("//*[contains(@id, 'map-popup-heading')]").text
print('Name collected')

time.sleep(5)
price = browser.find_element_by_id('map-popup-price').text
print('Price collected')

# enter data into database
cursor.execute('insert into tProducts (productName, productSeller, productPrice) values ("' + name + '", "' + website + '", "' + price + '");')
connection.commit()
print('H10 13S entered into database')
browser.quit()


# get product info for ASA airclassics HS-1A
