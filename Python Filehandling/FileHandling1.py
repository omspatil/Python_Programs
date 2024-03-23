stud_dict = {}

fobj = open("details.txt", "a")


def show_details(v):
    # (""Name": name, "Mob no.": mno, "Class": cl, "E-mail": email, "Average Marks": avg")
    return v["Name"] + "\t" + v["Mob no."] + "\t" + v["Class"] + "\t" + v["E-mail"] + "\t" + v["Average Marks"] + "\t"


def add_to_file(x):
    for k, v in x.items():
        fobj.write(str(k) + "\t:\t" + show_details(v))


def read_file(x):
    fobj.readline()



def add_new_stud():
    # logic to accept student info and it as dictionary into stud_dict{}
    # keep enrollment number as "key"
    name = input("Enter Name:")
    cl = input("Enter Class:")
    mno = input("Enter Your Mobile Number:")
    email = input("Enter Your Email:")
    prn = input("Enter Enrollment(PRN) Number:")
    avg = input("Enter Your Average Marks:")
    info = {"Name": name, "Mob no.": mno, "Class": cl, "E-mail": email, "Average Marks": avg}
    stud_dict[prn] = info
    add_to_file(stud_dict)


def update_stud(prn):
    # ask for enrollment number and update existing student information.
    # it should not add  new student, if enrollment number is not present in dictionary.
    if prn in stud_dict.keys():
        temp = stud_dict[prn]
        while True:
            print("Select an option")
            print("1 - Update Name")
            print("2 - Update Mob No.")
            print("3 - Update Class")
            print("4 - Update Email")
            print("5 - Update Average Marks")
            print("6 - Exit If Updated")
            ch = int(input("Provide your choice : "))
            if ch == 1:
                name = input("Enter Name:")
                temp["Name"] = name
            elif ch == 2:
                mno = input("Enter Your Mobile Number:")
                temp["Mob no."] = mno
            elif ch == 3:
                cl = input("Enter Class:")
                temp["Class"] = cl
            elif ch == 4:
                email = input("Enter Your Email:")
                temp["E-mail"] = email
            elif ch == 5:
                avg = input("Enter Your Average Marks:")
                temp["Average Marks"] = avg
            elif ch == 6:
                break
        # info = {"Name": name, "Mob no.": mno, "Class": cl, "E-mail": email, "Average Marks": avg}
        stud_dict[prn] = temp
    else:
        print("Enrollment Number Not Found.....")


def remove_stud_info(prn):
    # ask for enrollment number of student and delete that student info from dictionary.
    if prn in stud_dict.keys():
        del stud_dict[prn]
    else:
        print("Enter Valid Enrollment.... Entered Number is Invalid....")


def show_stud_info(pn):
    # ask for enrollment number and print all information of that student from dictionary.
    temp = stud_dict[pn]
    if pn in stud_dict.keys():
        # {"Name": name, "Mob no.": mno, "Class": cl, "E-mail": email, "Average Marks": avg}
        print("Name of Student:", temp["Name"])
        print("Mobile Number:", temp["Mob no."])
        print("Class:", temp["Class"])
        print("Email id:", temp["E-mail"])
        print("Average Marks:", temp["Average Marks"])

    else:
        print("Entered PRN Number Not Found....")


def show_all_stud():
    # show all student's information in table format
    print("Name     Class       Email       Mobile      AverageMarks")
    for key, value in stud_dict.items():
        temp = stud_dict[key]
        print(
            f"""{temp["Name"]}     {temp["Class"]}       {temp["E-mail"]}       {temp["Mob no."]}      {temp["Average Marks"]}""")


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
        add_new_stud()
    elif ch == 2:
        prn = input("Enter Enrollment No. to Update:")
        update_stud(prn)
    elif ch == 3:
        prn = input("Enter Correct Enrollment No. to Delete Data:")
        remove_stud_info(prn)
    elif ch == 4:
        prn = input("Enter Correct Enrollment No. to Show Data:")
        show_stud_info(prn)
    elif ch == 5:
        show_all_stud()
    elif ch == 6:
        exit(0)
