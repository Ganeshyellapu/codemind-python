import math
t=int(input())
for i in range(t):
    def lcm(a,b):
        if(a>b):
            lcm=a
        else:
            lcm=b
        if(lcm%a==0 and lcm%b==0):
            k=lcm
        else:
            lcm+=1
        return lcm
    n,a,b,k=map(int,input().split())
    c=((n/a)+(n/b))-(n/lcm(a,b))
    if(c>=k):
        print("Win")
    else:
        print("Lose")
    