n=int(input())
n1=0
n2=1
for i in range(2,n):
    n3=n1+n2
    if(n3>n):
        a=n3
        b=n2
        break
    n1=n2
    n2=n3
if(abs(n-a)>abs(n-b)):
    print(b)
elif (abs(n-a)==abs(n-b)):
    print(b,a)
else:
    print(a)