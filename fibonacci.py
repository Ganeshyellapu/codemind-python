n=int(input())
n1=0
n2=1
print(n1,end=' ')
print(n2,end=' ')
n3=0
for i in range(2,n):
    n3=n2+n1
    print(n3,end=' ')
    n1=n2
    n2=n3