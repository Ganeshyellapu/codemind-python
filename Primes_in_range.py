def isprime(k):
    if k==1:
        return False
    else:
        for j in range(2,int(k**0.5)+1):
            if k%j==0:
                return False
        else:
            return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if isprime(i):
        c=c+1
print(c)