def isprime(k):
    if k==1:
        return False
    else:
        for l in range(2,int(k**0.5)+1):
            if k%l==0:
                return False
                break
        else:
            return True
n=int(input())
a=list(map(int,input().split()))
b=max(a)
c=min(a)
d=0
e=0
s=0
for i in range(0,n):
    if a[i]==c:
        d=d+i
    elif a[i]==b:
        e=e+i
if d<e:
    for j in range(d,e+1):
        if isprime(a[j]):
            s=s+1
else:
    for j in range(e,d+1):
        if isprime(a[j]):
            s=s+1
print(s)
