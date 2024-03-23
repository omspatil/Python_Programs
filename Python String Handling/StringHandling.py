s1 = input('Enter a String:')
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for x in s1:
    a = ord(x)
    if a >= 65 and a <= 90:
        c1 = c1+1
    elif a >= 97 and a <= 122:
        c2 = c2+1
    elif a == 32:
        c3 = c3+1
    else:
        c4 = c4+1
print('Capital', c1)
print('Small', c2)
print('Space', c3)
print('Digit', c4)