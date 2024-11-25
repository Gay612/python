import pymysql
db=pymysql.connect(
host="localhost",
user="root",
passwd="password",
database="cs")
excursor=db.cursor()
sql1="update data base SET course = 'c' where name='gayu'"
try:
    excursor.execute(sql1)
    db.commit()
except:
    db.rollback
