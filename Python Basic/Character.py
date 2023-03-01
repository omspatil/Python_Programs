#Checking given character is Capital Case or Small Case or Digit
n=input("Enter Any Character: ")

if(65<=ord(n)<=90):
    print('Capital')
elif (97<=ord(n)<=122):
    print('Small')
else:
    print('Digit')

