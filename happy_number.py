def isdigit(k):
    s=0
    while(k):
        r=k%10
        s=s+r*r
        k=k//10
    if(s<=9):
        return s
    else:
        k=isdigit(s)
        return k
n=int(input())
m=isdigit(n)
if m==1 or m==7:
    print("True")
else:
    print("False")