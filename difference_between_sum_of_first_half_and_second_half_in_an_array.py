n=int(input())
a=list(map(int,input().split()))
s=0
c=0
if n%2!=0:
    for i in range(0,n//2):
        s=s+a[i]
    for i in range(n//2,n):
        c=c+a[i]
elif n%2==0:
    for i in range(0,n//2):
        s=s+a[i]
    for i in range(n//2,n):
        c=c+a[i]
print(abs(c-s))
