from tkinter import *
def show():
    l1['text']='Hello World'
root=Tk()
root.geometry("500x500")
root.title("first root win")
f=Frame(root,height=500,width=500,bg="black")
f.pack(fill=BOTH,expand=TRUE)
l1=Label(f,text="Hi There",bg="yellow",font=('times new roman',25,))
l1.pack()
b1=Button(f,text='click here',width=20,command=show)
b1.pack()
root.mainloop()

