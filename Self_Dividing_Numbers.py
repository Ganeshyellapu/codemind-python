a=int(input())
b=int(input())
for i in range(a,b+1):
    s=0
    c=len(str(i))
    q=i
    while(q):
        r=q%10
        if r!=0:
            if i%r==0:
                s=s+1
        q=q//10
    if(s==c):
        print(i,end=' ')