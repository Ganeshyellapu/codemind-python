n=list(input())
a=list(map(int,input().split()))
k=set(a)
d=list(k)
d.sort()
m=int(input())
c=0
s=[]
for i in d:
    if a.count(i)==m:
        c=c+1
        s.append(i)
if c>0:
    print(*s)
else:
    print("-1")