""" Consider following dictionary and write the main script to generate a list contains the keys that 
continuously occurs specified times as its value.
Given dictionary: dict1 = {1:3, 2:5, 4:5:, 7:3, 11:7, 13:2}
Expected output: ls = [1,1,1,2,2,2,2,2,4,4,4,4,4,7,7,7,11,11,11,11,11,11,11,13,13]
"""
dict1 = {1: 3, 2: 5, 4: 5, 7: 3, 11: 7, 13: 2}
ls = []
for key, value in dict1.items():
    ls += [key] * value
print(ls)