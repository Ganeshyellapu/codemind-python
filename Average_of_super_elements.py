n=list(input())
a=list(map(int,input().split()))
k=set(a)
c=0
s=0
for i in k:
    if a.count(i)==i:
        c=c+1
        s=s+i
if c>=1:
    k=s/c
    print('{:.2f}'.format(k))
else:
    print("-1")
