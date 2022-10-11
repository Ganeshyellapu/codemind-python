n=int(input())
k=n*n
s=0
while k:
    r=k%10
    s=s+r
    k=k//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")