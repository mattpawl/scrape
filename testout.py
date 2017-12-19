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

def shorten(s, subs):
    i = s.index(subs)
    return s[:i+len(subs)]
website = shorten("http://www.sportys.com/pilotshop/david-clark-h10-13-4-headset.html", '.com')
name = "name"
price = "10"

cursor.execute('insert into tProducts (productName, productSeller, productPrice) values ("' + name + '", "' + website + '", "' + price + '");')
connection.commit()
