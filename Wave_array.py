n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n-2):
    if ((a[i]>a[i+1] and a[i+1]<a[i+2]) or (a[i]<a[i+1] and a[i+1]>a[i+2])):
        c=c+1
if c==n-2:
    print('yes')
else:
    print('no')