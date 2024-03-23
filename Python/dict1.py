"""Consider following dictionary as local variable of a user-defined function. This function contains one 
parameter/argument. Prepare body of this function to check whether specified parameter is present as 
key or as value in that dictionary. 
dict1 = {“one”: 10, “two”: 20, “three”: 30, “four”: 40, “five”: 50, “six”: 60}
If it is present as key or value then return True otherwise return False.
Also write main script to test working of this function."""

dict1 = {"one": 10, "two": 20, "three": 30, "four": 40, "five": 50, "six": 60}


def check(x):
    d1 = dict1.values()
    d2 = dict1.keys()
    if x in d1 or x in d2:
        return True
    else:
        return False


a = check(50)
b = check("one")
print(a)
print(b)
print(check(70))
