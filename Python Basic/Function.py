def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

print('Enter Two Numbers')
a,b=map(int,input().split())

print('Addition:',add(a,b))
print('Subtraction:',sub(a,b))
print('Division:',div(a,b))
print('Multiplication:',mul(a,b))
