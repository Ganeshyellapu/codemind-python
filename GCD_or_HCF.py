def gcd(a,b):
    for i in range(1,a+b+1):
        if a%i==0 and b%i==0:
            hcf=i
    print(hcf)
a,b=map(int,input().split())
gcd(a,b)