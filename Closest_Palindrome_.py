def isplan(k):
    e=k
    s=0
    while(e):
        r=e%10
        s=s*10+r
        e=e//10
    if s==k:
        return True
    else:
        return False
n=int(input())
q=n
h=n
while(True):
    n=n+1
    if isplan(n):
        p=n
        break
while(True):
    q=q-1
    if isplan(q):
        m=q
        break
if(p-h>h-m):
    print(m)
elif(p-h==h-m):
    print(m,p)
else:
    print(p)
