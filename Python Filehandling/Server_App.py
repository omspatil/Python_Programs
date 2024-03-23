def operation(x, y, op):
    if op == "+\n":
        v = x + y
        s = str(x) + " + " + str(y) + " = " + str(v) + "\n"
        return s
    elif op == "-\n":
        v = x - y
        s = str(x) + " - " + str(y) + " = " + str(v) + "\n"
        return s
    elif op == "*\n":
        v = x * y
        s = str(x) + " * " + str(y) + " = " + str(v) + "\n"
        return s
    elif op == "/\n":
        v = x / y
        s = str(x) + " / " + str(y) + " = " + str(v) + "\n"
        return s
    elif op == "%\n":
        v = x % y
        s = str(x) + " % " + str(y) + " = " + str(v) + "\n"
        return s
    elif op == "**\n":
        v = x ** y
        s = str(x) + " ** " + str(y) + " = " + str(v) + "\n"
        return s


def write_to_file(n_d):
    fobj = open("Operations.txt", "w")
    fobj.writelines(n_d)
    fobj.close()


def perform_op(temp):
    num1 = int(temp[0])
    num2 = int(temp[1])
    op = temp[2]
    final = operation(num1, num2, op)
    return final


# def write(n_d):
#     fobj = open("Operations.txt", "a")
#     fobj.writelines(n_d)
#     fobj.close()


fobj = open("Operations.txt", "r")
data = fobj.readlines()
fobj.close()
temp = []
j = 0
new_data = []
for i in range(len(data)):
    if "," in data[i]:
        ls = data[i].split(",")
        temp.append(ls)
        # print(type(perform_op(ls)))
        # ['200', '300', '+\n']
        # ['400', '300', '-\n']
        # ['45', '2', '*\n']
        str_data = perform_op(ls)
        data[i] = str_data
        # write_to_file(str_data)
    else:
        # write(data[i])
        continue
write_to_file(data)
print("....Data Updated Successfully....")
