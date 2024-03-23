def write_to_file(s):
    fobj = open("Operations.txt", "a")
    fobj.writelines(data)
    fobj.close()
    print(".....Data Pushed.....")
    input("Enter To Proceed")


input("............PRESS ENTER TO START THE APPLICATION...........")
while True:

    print("Enter 1 to Perform Calculations or 0 to Exit")
    i = int(input("Enter 0 or 1 :"))
    if i == 1:
        operands = input("Enter Two Operands to Perform Operation: ")
        num1, num2 = operands.split(" ")
        op = input("Enter Operand (+ , - , * , ** , / , %) :")
        data = num1 + "," + num2 + "," + op + "\n"
        write_to_file(data)
    elif i == 0:
        exit(0)
