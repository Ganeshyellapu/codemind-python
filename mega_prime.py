def isprime(k):
    if k==1:
        return False
    for i in range(2,k//2+1):
        if k%i==0:
            return False
            break
    else:
        return True
n=int(input())
c=0
k=0
f=0
if(isprime(n)):
    f=1
    q=n
    while q:
        r=q%10
        if isprime(r):
            k=k+1
        c=c+1
        q=q//10
else:
    print("Not Mega Prime")
if(f==1):
    
    
    if k==c:
        
        print("Mega Prime")
    else:
        print("Not Mega Prime")