"""Consider following list and prepare a dictionary contains unique values as key and their count as it’s
values.
ls = [1, 2, 3, 2, 2, 4, 5, 6, 5, 4, 2, 1, 3, 4, 5, 5, 6, 7, 7, 8, 1, 3, 4, 5, 7, 5]
Expected output : 
dict1 = {1:3 , 2:4, 3:3, 4:4, 5:6, ….. }
"""
ls = [1, 2, 3, 2, 2, 4, 5, 6, 5, 4, 2, 1, 3,
      4, 5, 5, 6, 7, 7, 8, 1, 3, 4, 5, 7, 5]
dict1 = {}
for i in ls:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)

#################################
d = {}
for x in ls:
    a = ls.count(x)
    d[x] = a
print(d)
