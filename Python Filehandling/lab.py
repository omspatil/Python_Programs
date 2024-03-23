from datetime import date as dt


def _check(bn, ls):
    for i in range(len(ls)):
        temp = ls[i].split(",")
        if bn == temp[1] and temp[3] == "NA":
            temp[3] = get_date()
            temp[4] = 'R'
            return i, temp, True


def return_book():
    bno = input("Enter Book Number:")
    fobj = open("all_issued.txt", "r")
    book_list = fobj.readlines()
    fobj.close()
    i, ls, check = _check(bno, book_list)

    if check:
        str = ",".join(ls)
        book_list[i] = str
        fobj = open("all_issued.txt", "w")
        fobj.writelines(book_list)
        fobj.close()
    print("Book Returned Successfully......")


def get_date():
    obj = dt.today()
    d = obj.day
    m = obj.month
    y = obj.year
    today_dt = str(d) + "/" + str(m) + "/" + str(y)
    return today_dt


def issue_book():
    enr = input("Enter Enrollment Number of Borrower : ")
    bnum = input("Enter Book Number to Borrow : ")
    i_date = get_date()
    fobj = open("all_issued.txt", "a")
    fobj.write(enr + "," + bnum + "," + i_date + "," + "NA" + "," + "P\n")
    fobj.close()
    print("Book Issued...")
    input()


def show_not_ret_books():
    """
    print pending status books
    :return:
    """
    fobj = open("all_issued.txt", "r")
    issued_list = fobj.readlines()
    fobj.close()
    for i in range(len(issued_list)):
        temp = issued_list[i].split(",")
        if temp[4] == 'P\n':
            print(temp[0], temp[1], temp[2], sep="\t\t")
    input("\nEnter To Proceed....\n")


def add_new_stud():
    name = input("Enter Name:")
    cl = input("Enter Class:")
    mno = input("Enter Your Mobile Number:")
    prn = input("Enter Enrollment(PRN) Number:")
    fobj = open('all_stud.txt', 'a')
    fobj.write(prn + "," + name + "," + cl + "," + mno + "\n")
    fobj.close()
    print("....Student Data Added....")


def add_new_book():
    b_no = input("Enter Book Number:")
    b_title = input("Enter Title: ")
    b_author = input("Enter Author: ")
    b_pub = input("Enter Publication: ")
    fobj = open('all_books.txt', 'a')
    fobj.write(b_no + "," + b_title + "," + b_author + "," + b_pub + "\n")
    fobj.close()
    print("....Book Added....")


def stud_history():
    prn = input("Enter Enrollment Number to Check:")
    fobj = open("all_issued.txt", "r")
    ls = fobj.readlines()
    fobj.close()

    for i in range(len(ls)):
        temp = ls[i].split(",")
        if prn == temp[0]:
            print(temp[1], temp[2], temp[3], sep="\t\t")
            check = True


def book_history(bno):
    fobj = open("all_issued.txt", "r")
    book_list = fobj.readlines()
    fobj.close()
    count = 0
    for i in range(len(book_list)):

        temp = book_list[i].split(",")
        if bno == temp[1]:
            count += 1
            print(temp[0], temp[2], temp[3], sep="\t\t")
            check = True
    print("This Book have Issued", count, "times")
    if not check:
        book_history(input("Enter Again: "))
    input("\nEnter To Proceed....\n")


def get_by_title(ls, x):
    for i in range(len(ls)):
        temp = ls[i].split(",")
        if x == temp[1]:
            print(temp[0], temp[2], temp[3], sep="\t\t", end="")
            check = True
    if not check:
        get_by_title(ls, input("Enter Again:"))


def get_by_author(ls, x):
    for i in range(len(ls)):
        temp = ls[i].split(",")
        if x == temp[2]:
            print(temp[0], temp[1], temp[3], sep="\t\t", end="")
            check = True
    if not check:
        get_by_author(ls, input("Enter Again:"))


def get_by_pub(ls, x):
    for i in range(len(ls)):
        temp = ls[i].split(",")
        if x == temp[3]:
            print(temp[0], temp[1], temp[2], sep="\t\t")
            check = True
    if not check:
        get_by_pub(ls, input("Enter Again:"))


def search_book():
    fobj = open("all_books.txt", "r")
    book_list = fobj.readlines()
    fobj.close()
    print("Search Book By Below options:")
    print("1 - By Book Title")
    print("2 - By Book Author")
    print("3 - By Book Publications")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        t = input("Enter Title")
        get_by_title(book_list, t)
    elif ch == 2:
        a = input("Enter Author")
        get_by_author(book_list, a)
    elif ch == 3:
        p = input("Enter Name of Publication")
        get_by_pub(book_list, p)

def stud(prn, ls):
    for i in range(len(ls)):
        temp = ls[i].split(",")
        if prn == temp[0]:
            return i, temp, True
def search_stud():
    prn=input("Enter Enrollment Number: ")
    fobj = open("all_stud.txt", "r")
    stud_list = fobj.readlines()
    fobj.close()
    i, ls, check = stud(prn, stud_list)
    print("""Name is :"""+ls[1]+"""
Class is : """+ls[2]+"""
Mobile number is : """+ls[3]+"""
Email is : """+ls[4])
    if not check:
        search_stud()
while True:
    print("Select an option")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Add New Student")
    print("4 - Add New Book")
    print("5 - Show Not Returned Books")
    print("6 - Student History")
    print("7 - Book History")
    print("8 - Search Book")
    print("9 - Search Student")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch == 1:
        issue_book()
    elif ch == 2:
        return_book()
    elif ch == 3:
        add_new_stud()
    elif ch == 4:
        add_new_book()
    elif ch == 5:
        show_not_ret_books()
    elif ch == 6:
        stud_history()
    elif ch == 7:
        x = input("Enter Book Number:")
        book_history(x)
    elif ch == 8:
        search_book()
    elif ch == 9:
        search_stud()
    elif ch == 0:
        exit(0)
