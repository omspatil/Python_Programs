"""Consider following dictionary and print the sum of all keys and values of it.
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""


dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
a = dict1.keys()
b = dict1.values()
print(sum(a)+sum(b))
