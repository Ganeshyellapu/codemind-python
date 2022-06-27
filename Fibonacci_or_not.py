n=int(input())
n1=0
n2=1
for i in range(2,n+1):
    n3=n1+n2
    if(n3==n):
        print(True)
        break
    n1=n2
    n2=n3
else:
    print(False)