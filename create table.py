import pymysql
db=pymysql.connect(
host="localhost",
user="root",
passwd="password",
database="cs")
excursor=db.cursor()
excursor.execute("CREATE table data (name varchar(20), course varchar(10), duration varchar(3))")
        

