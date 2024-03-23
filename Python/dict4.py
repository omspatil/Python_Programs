"""Consider following dictionary and list and write the main script to remove the keys from dictionary 
which are specified in list.
dict1 = {“one”: 10, “two”: 20, “three”: 30, “four”: 40, “five”: 50, “six”: 60}
ls = [“three”, “five”]
"""

dict1 = {"one": 10, "two": 20, "three": 30, "four": 40, "five": 50, "six": 60}
ls = ["three", "five"]
for x in ls:
    dict1.pop(x)
print(dict1)
