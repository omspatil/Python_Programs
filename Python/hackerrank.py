"""def solve(arr, N):
    arr.sort()
    a = 0
    b = 0
    for i in range(N):

        
        if (i % 2 != 0):
            a = a * 10 + arr[i]
        else:
            b = b * 10 + arr[i]
    return a + b
if __name__ == '__main__':
    a=int(input())
    arr = [int(x) for x in str(a)]
    N = len(arr)
    print( solve(arr, N))
"""
##########################################33
"""k=list(input())
N=(input())
N=[int(i) for i in N.split()]
ls=[]
for i in range(len(N)):
    x=max(N)
    y=min(N)
    if N[i] is x:
        ls.append(1)
    else:
        ls.append(0)

listToStr = ' '.join([str(elem) for elem in ls])
print(listToStr)
"""
#####################################################

def check(str1, str2, str3):
    
    
    mark = [False for i in range(26)]
    
    n = len(str1)
    m = len(str2)
    o=len(str3)
    
    for i in range(n):
        mark[ord(str1[i]) - ord('a')] = True
    
    # Check if any of the character
    # of str2 is already marked
    for i in range(o):
        mark[ord(str3[i]) - ord('a')] = True
    for i in range(m):
        
        # If a common character
        # is found
        if (mark[ord(str2[i]) - ord('a')]):
            return True;

    # If no common character
    # is found
    return False
    
# Driver code
if __name__=="__main__":
    
    str1 =input()
    str2 =input()
    str3=input()

    if (check(str1, str2,str3)):
        print("true");
    else:
        print("false");


