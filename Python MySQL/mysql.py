import pymysql as mysql
con = mysql.connect(user='root', password='root',database='employees', host='localhost')
c = con.cursor()
id = int(input('enter id:'))
name = input('enter name:')
sql = "insert into information values(%s,%s)"
arr = (id, name)
c.execute(sql, arr)
con.commit()
print("record inserted ")
con.close()
