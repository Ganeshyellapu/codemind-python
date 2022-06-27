def isprime(k):
    if k==1:
        return False
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    else:
        return True
n=int(input())
for i in range(2,n//2+1):
    if isprime(i):
        c=n//i
        if isprime(c) and c>i and c*i==n:
            z=c
            x=i
            print(x,z)
            break
else:
    print('-1')
            