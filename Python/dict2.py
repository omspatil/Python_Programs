""" Consider following dictionary and write the main script to print only unique values from it.
 dict1 = {
'list1': [4, 7, 10, 20], 
 'list2': [7, 16, 9, 10], 
 'list3': [13, 10, 4, 8], 
'list4': [7, 20, 6, 11]
}
Expected Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]
"""

dict1 = {
    'list1': [4, 7, 10, 20],
    'list2': [7, 16, 9, 10],
    'list3': [13, 10, 4, 8],
    'list4': [7, 20, 6, 11]
}
a = list(dict1.values())
print(a)

b = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] not in b:
            b.append(a[i][j])
b.sort()
print(b)
