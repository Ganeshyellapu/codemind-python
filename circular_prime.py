def isprime(k):
    c=0
    if k==1:
        c=0
        return c
    else:
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                c=0
                return c
                break
        else:
            c=1
            return c
n=int(input())
q=n
s=0
while q:
    r=q%10
    s=s*10+r
    q=q//10
if isprime(n)==1 and isprime(s)==1:
    print("circular prime")
elif isprime(n)==1 and isprime(s)!=1:
    print("prime but not a circular prime")
else:
    print("not prime")