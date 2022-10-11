n=int(input())
q=n
s=0
if q<0:
    q=q*-1
    while q:
        r=q%10
        s=s*10+r
        q=q//10
    print(s*-1)
else:
    while(q):
        r=q%10
        s=s*10+r
        q=q//10
    print(s)