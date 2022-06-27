n=list(input())
a=list(map(int,input().split()))
k=set(a)
d=list(k)
c=0
s=[]
for i in d:
    if a.count(i)==i:
        c=c+1
        s.append(i)
if c>=1:
    print(min(s),max(s))
else:
    print("-1")
