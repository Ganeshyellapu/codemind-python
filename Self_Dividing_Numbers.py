def pretty(x,y):
    if x==0:
        return False
    elif y%x==0:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    k=0
    q=i
    while(q):
        r=q%10
        c=c+1
        if pretty(r,i):
            k=k+1
        q=q//10
    if c==k:
        print(i,end=" ")
    c=0
    k=0