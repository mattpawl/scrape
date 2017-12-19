import pymysql
import time
# connection to mysql
connection = pymysql.connect(host='localhost',
                                  user='root',
                                  password='admin',
                                  db='Products')
# cursor used to exec queries
cursor = connection.cursor()
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


# write data to table
cursor.execute('select * from tSportys;')
sportys_data = cursor.fetchall()
cursor.execute('select * from tAircraftSpruce;')
aircraftspruce_data = cursor.fetchall()
cursor.execute('select * from tMarvGolden;')
marvgolden_data = cursor.fetchall()
count = 0
for row in sportys_data:
    spruce = aircraftspruce_data[count]
    marv = marvgolden_data[count]
    count += 1
    file.write('\n    <tr>')
    file.write('\n        <td>' + row[1] + '</td>')
    file.write('\n        <td>' + row[2] + '</td>')
    file.write('\n        <td><a href="' + row[4] + '" target="_blank">' + row[3] + '</td>')
    file.write('\n        <td><a href="' + spruce[2] + '" target="_blank">' + spruce[1] + '</td>')
    file.write('\n        <td><a href="' + spruce[2] + '" target="_blank">' + marv[1] + '</td>')
    file.write('\n        <td>Pilot price</td>')
    file.write('\n        <td>Gulf price</td>')
    file.write('\n        <td>Amazon price</td>')
    file.write('\n        <td>Skygeek price</td>')
    file.write('\n    </tr>')
# file.write('\n        <td><a href="' + product_url + '" target="_blank">' + product_price + '</td>')
# write tAircraftSpruce data to table

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

