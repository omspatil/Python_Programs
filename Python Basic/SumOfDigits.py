#Sum of digits of given number
n=int(input("Enter Any Number: "))

sum=0
while n>0:
    n1=n%10
    n=n//10
    sum+=n1
print(" Sum Of Digits: ",sum)