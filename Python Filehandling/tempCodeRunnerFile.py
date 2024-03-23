def AddNewStud():
    prn = input("Enter PRN Number:")
    name = input("Enter Name:")
    mob = input("Enter Your Mobile Number:")
    email = input("Enter Your Email:")
    
    fobj=open("C:\\Users\\91973\\OneDrive\\Documents\\Student.txt","a")
    fobj.writelines(prn+","+name+","+mob+","+email+"\n")
    fobj.close()
    
    
def Update():
    prn = input("Enter PRN Number:")
    fobj=open("C:\\Users\\91973\\OneDrive\\Documents\\Student.txt","r")
    ls=fobj.readlines()
    fobj.close()
    for i in range(len(ls)):
        temp=ls[i].split(",")
        if prn ==temp[0]:
            flag=True
    if flag:
        temp[1] = input("Enter Name:")
        temp[2] = input("Enter Your Mobile Number:")
        temp[3] = input("Enter Your Email:")
    str=",".join(temp)
    ls[i]=str
    fobj=open("C:\\Users\\91973\\OneDrive\\Documents\\Student.txt","w")
    fobj.writelines(ls)
    fobj.close()
def Remove(prn):
    pass
def ShowOne(prn):
    a=prn
    fobj=open("C:\\Users\\91973\\OneDrive\\Documents\\Student.txt","r")
    if a==a[0]:
        return True
    else:
        return False
def ShowAll():
    fobj=open("C:\\Users\\91973\\OneDrive\\Documents\\Student.txt","r")
    fobj.readlines()
    fobj.close()

while True:
    print("Select an option")
    print("1 - Add New Student")
    print("2 - Update Student Info")
    print("3 - Remove Student Info")
    print("4 - Show Student Info")
    print("5 - Show All Students")
    print("6 - Exit")
    ch = int(input("Provide your choice : "))

    if ch == 1:
        AddNewStud()
    elif ch == 2:
        
        Update()
    elif ch == 3:
        prn = input("Enter Correct Enrollment No. to Delete Data:")
        Remove(prn)
    elif ch == 4:
        prn = input("Enter Correct Enrollment No. to Show Data:")
        ShowOne(prn)
    elif ch == 5:
        ShowAll()
    elif ch == 6:
        exit(0)
"""
def update_stud_info():
    stud_found=False
    enr=input("enter enr")
    fobj=open("","r")
"""