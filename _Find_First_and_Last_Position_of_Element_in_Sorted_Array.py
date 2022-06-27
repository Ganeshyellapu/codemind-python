n=int(input())
l=list(map(int,input().split()))
k=int(input())
c,c1=0,0
for i in range(len(l)):
    if k==l[i]:
        t1=i
        c=1
        break
if c==0:
    t1=-1
for i in range(len(l)-1,-1,-1):
    if k==l[i]:
        t2=i
        c1=1
        break
if c1==0:
    t2=-1
print(t1,t2)