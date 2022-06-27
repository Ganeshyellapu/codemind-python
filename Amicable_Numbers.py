a=int(input())
b=int(input())
s=0
c=0
for i in range(1,a//2+1):
    if a%i==0:
        s=s+i
for j in range(1,b//2+1):
    if b%j==0:
        c=c+j
if s==b and c==a:
    print("Amicable")
else:
    print("Not Amicable")