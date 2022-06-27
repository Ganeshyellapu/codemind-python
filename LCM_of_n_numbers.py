def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
n=int(input())
l=list(map(int,input().split()))
lcm=l[0]
for i in range(1,n):
    lcm=(l[i]*lcm)//hcf(l[i],lcm)
print(int(lcm))