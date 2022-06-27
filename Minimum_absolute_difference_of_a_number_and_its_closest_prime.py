import math
def isprime(k):
    for i in range(2,int(math.sqrt(k)+1)):
        if k%i==0:
            return False
            break
    else:
        return k
n=int(input())
q=n
z=n
f=0
if isprime(n):
    print('0')
else:
    while True:
        n=n+1
        if isprime(n):
            break
    m=isprime(n)
    while True:
        q=q-1
        if isprime(q):
            break
    a=isprime(q)
    if z-a>m-z:
        print(m-z)
    elif z-a==m-z:
        print(m-z)
    else:
        print(z-a)
