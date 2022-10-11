def isnonprime(k):
    for j in range(2,int(k**0.5)+1):
        if k%j==0:
            return True
    else:
        return False
n=int(input())
c=0
for i in range(2,n+1):
    if n%i==0:
        if isnonprime(i):
            c=c+1
print(c+1)