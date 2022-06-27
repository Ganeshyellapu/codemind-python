def hcf(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
n=int(input())
l=list(map(int,input().split()))
v=l[0]
for i in range(1,n):
    v=hcf(l[i],v)
print(v)