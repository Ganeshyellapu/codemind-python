def isdigit(k):
    s=0
    while(k):
        r=k%10
        s=s+r
        k=k//10
    if(s<=9):
        return s
    else:
        k=isdigit(s)
        return k
n=int(input())
#print(n)
if n<=9:
    print(n)
else:
    print(isdigit(n))