a=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
m=set(c)
k=set(d)
c=0
h=0
for i in m:
    if i not in k:
        c=c+1
for j in k:
    if j not in m:
        h=h+1
print(c+h)