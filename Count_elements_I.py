a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in range(0,a):
    for j in range(0,b):
        if c[i]==d[j]:
            e.append(c[i])
            c[i]=-1
            d[j]=0
f=[]
h=0
for i in e:
    if i not in f:
        f.append(i)
        h=h+1
print(h)
    