def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
def ispalan(k):
    q=k
    s=0
    while(q):
        r=q%10
        s=s*10+r
        q=q//10
    if s==k:
        return True
    else:
        return False
n=int(input())
while(True):
    n=n+1
    if ispalan(n) and isprime(n):
        print(n)
        break