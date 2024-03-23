from tkinter import *
import pymysql as mysql
root = Tk()
root.title("Entry Form")
root.geometry('500x500')


def save():

    con = mysql.connect(user='root', password='root',
                        database='employees', host='localhost')
    c = con.cursor()
    id = id1.get()
    name = name1.get()
    sql = "insert into information values(%s,%s)"
    arr = (id, name)
    c.execute(sql, arr)
    con.commit()


def update():
    con = mysql.connect(user='root', password='root',
                        database='employees', host='localhost')

    c = con.cursor()
    id = id1.get()
    name = name1.get()
    sql = "update information set name=%s where id=%s"
    arr = (name, id)
    c.execute(sql, arr)
    con.commit()


def delete():
    con = mysql.connect(user='root', password='root',
                        database='employees', host='localhost')

    c = con.cursor()
    id = id1.get()
    name = name1.get()
    sql = 'delete from information where id=%s'
    arr = (id,)
    c.execute(sql, arr)
    con.commit()


def select():
    con = mysql.connect(user='root', password='root',
                        database='employees', host='localhost')

    c = con.cursor()
    id = id1.get()
    sql = 'select * from information where id=%s'
    arr = (id,)
    c.execute(sql, arr)
    row = c.fetchone()
    if row == None:
        print('Record not found')
        name1.insert(0, 'record not found')

    else:
        print(row[1])
        name1.insert(0, row[1])
    con.close()
def clear():
    name.delete(0,END)
    name1.delete(0,END)

     

screen = Frame(root, height=500, width=500, bg="white")
screen.pack(fill=BOTH, expand=True)
# lable
Label(screen, text="Entry form", font='arial 20 bold',
      bg='black', fg='white').pack(fill='both')
Label(screen, text="ID", font='30').place(x=200, y=200)
Label(screen, text="NAME", font='30').place(x=200, y=300)
# Entry
id1 = StringVar()
name1 = StringVar()
name = Entry(screen, font='20', bd=4, textvariable=id1)
name1 = Entry(screen, font='20', bd=4, textvariable=name1)
name.place(x=375, y=200)
name1.place(x=375, y=300)
# button
Button(screen, text='SAVE', font='20', command=save).place(x=200, y=400)
Button(screen, text='UPDATE', font='20', command=update).place(x=400, y=400)
Button(screen, text='DELETE', font='20', command=delete).place(x=600, y=400)
Button(screen, text='SELECT', font='20', command=select).place(x=800, y=400)
Button(screen, text='CLEAR', font='20', command=clear).place(x=1000, y=400)
root.mainloop()
