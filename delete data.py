import pymysql
db=pymysql.connect(
host="localhost",
user="root",
passwd="password",
database="cs")
excursor=db.cursor()
sql1="delete from data where name='gayu' "
try:
    excursor.execute(sql1)
    db.commit()
except:
    db.roolback
