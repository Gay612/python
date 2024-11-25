import pymysql
db=pymysql.connect(
host="localhost",
user="root",
passwd="password",
database="cs")
excursor=db.cursor()
excursor.execute("select  * from data")
res=excursor.fetchall()
print(res)
