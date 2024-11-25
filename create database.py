import pymysql
db=pymysql.connect(
host="localhost",
user="root",
passwd="password")
excursor=db.cursor()
excursor.execute("CREATE DATABASE cs")
