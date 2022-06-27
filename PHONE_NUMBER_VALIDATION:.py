n=int(input())
c=0
while n!=0:
    r=n%10
    c=c+1
    n=n//10
if c==10:
    print("Valid")
else:
    print("Invalid")