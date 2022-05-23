h,m=map(float,input().split(':'))
a=abs((30*h)-(5.5*m))
d=360-a
if d>a:
    print(a)
else:
    print(d)