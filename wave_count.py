n=int(input())
a=list(map(int,input().split()))
c=0
m=0
for i in range(0,n-2):
    if ((a[i]>a[i+1] and a[i+1]<a[i+2]) or (a[i]<a[i+1] and a[i+1]>a[i+2])):
        m=m+1
        if a[i]<a[i+1] and a[i+1]>a[i+2]:
            c=c+1
    else:
        print('-1')
        break
if m==n-2:
    print(c)