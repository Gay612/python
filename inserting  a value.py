import pymysql
db=pymysql.connect(
host="localhost",
user="root",
passwd="password",
database="cs")
excursor=db.cursor()
excursor.execute( """insert into data(name,course,duration) values('gayu','python','two'),('mahe','java','one')""")
db.commit()
