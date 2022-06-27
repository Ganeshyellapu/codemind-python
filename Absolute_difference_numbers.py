import math
n,a=map(int,input().split())
q=n
s=0
while q!=0:
    r=q%10
    s=s*10+r
    q=q//10

k=int(math.pow(10,a))
b=n%k
c=s%k
v=c
x=0
while v!=0:
    r1=v%10
    x=x*10+r1
    v=v//10
print(abs(x-b))