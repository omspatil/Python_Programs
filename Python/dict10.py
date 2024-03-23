"""Define a function that has variable-length keyword-arguments as parameter and this function must print
pyramid from following dictionary information:
dict1 = {“A”:5, “AB”:9, “XYZ”:3, “$”:5}
The keys indicate the content to be printed and the values indicates the numbers of rows to be printed."""

dict1 = {"A": 5, "AB": 9, "XYZ": 3, "$": 5}
for k, v in dict1.items():
    rows = v 
    x = 2 * rows - 2  # It is used for number of spaces  
    for i in range(0, rows):  
        for j in range(0, x):  
            print(end=" ")  
        x = x - 1   # decrement k value after each iteration  
        for j in range(0, i + 1):  
                    print(k, end="")  # printing star  
        print("")  





  


#########################################
"""ls1=[1,2,3,4,5]
ls2=['one','two','three','four','five']
a=dict(zip(ls1,ls2))
print(a)"""
#########################
