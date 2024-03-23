# Slicing and Dicing 
my_list = [1, 11, 5, 5, 7, 8, 1, 2, 4, 5, 0, 4, 1, 4, 5]
a=my_list[:]
print("my_list[:] :",a)
b=my_list[2:]
print("my_list[2:] :",b)
c=my_list[:2]
print("my_list[:2] :",c)
d=my_list[:2:-2]
print("my_list[:2:-2] :",d)
e=my_list[2:4]
print("my_list[2:4] :",e)
f=my_list[::2]
print("my_list[::2] :",f)
g=my_list[::-2]
print("my_list[::-2] :",g)
h=my_list[::]
print("my_list[::] :",h)
i=my_list[8:2]
print("my_list[8:2] :",i)
j=my_list[8::2]
print("my_list[8::2] :",j)
k=my_list[:8:2]
print("my_list[:8:2] :",k)
l=my_list[1::-2]
print("my_list[1::-2] :",l)
m=my_list[0::2]
print("my_list[0::2] :",m)
n=my_list[ -2: -7 : 2]
print("my_list[ -2: -7 : 2] :",n)
o=my_list[ -7: -2 : 2]
print("my_list[ -7: -2 : 2] :",o)
p=my_list[-7: -2: -2]
print("my_list[-7: -2: -2] :",p)
q=my_list[-2: -7: -2]
print("my_list[-2: -7: -2] :",q)