import pymysql

connection = pymysql.connect(host="127.0.0.1", password="12345", user="user", db="deliverys")

print(connection)


