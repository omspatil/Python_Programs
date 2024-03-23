from tkinter import *
def show():
    n=e1.get()
    l1['text']="Hello "+n
root=Tk()
root.geometry("500x500")
root.title("first root win")
f=Frame(root,height=500,width=500,bg="black")
f.pack(fill=BOTH,expand=TRUE)
e1=Entry(f,width=25)
e1.pack()
l1=Label(f,text="Hi There",bg="sky blue",font=('times new roman',18,))
l1.pack()
b1=Button(f,text='click here',width=20,command=show)
b1.pack()
root.mainloop()

