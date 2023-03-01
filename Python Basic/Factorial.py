#Factorial of given number
n=int(input("Enter Any Number:"))

i=1
fact=1

while i<=n:
    fact*=i
    i=i+1
print(fact)