n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)):
    s=s+a[i]
print(s)