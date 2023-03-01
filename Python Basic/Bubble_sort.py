# sorting a list by using Bubble Sort
x = []
n = int(input('Enter No. Of Elements For Creating List:'))

for i in range(n):
    x.append(int(input()))

# for i in range(n):
#     print(x[i],end=" ")

print('Original List:', x)

# BubbleSort Algorithm

flag = False
for i in range(n - 1):
    for j in range(n - 1 - i):
        if x[j] > x[j + 1]:
            temp = x[j]
            x[j] = x[j + 1]
            x[j + 1] = temp
            flag = True
    if flag:  # flag = false then break....
        break
    else:
        flag = False

print('Sorted List:', x)