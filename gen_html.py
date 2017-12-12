import pymysql
# database connecion and data extraction
connection = pymysql.connect(host='localhost',
                                  user='root',
				  password='admin',
				  db='Products')
# query
cursor = connection.cursor()

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
file.write('\n        <th>Product Name</th>')
file.write('\n        <th>Website</th>')
file.write('\n        <th>Price</th>')
file.write('\n    </tr>')
cursor.execute('select * from tProducts;')
data = cursor.fetchall()
for row in data:
    product_name = row[1]
    product_seller = row[2]
    product_price = str(row[3])
    file.write('\n    <tr>')
    file.write('\n        <td>' + str(product_name) + '</td>')
    file.write('\n        <td>' + str(product_seller) + '</td>')
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
