import math
n=int(input())
c=0
q=n
while(q):
    r=q%10
    c=c+1
    q=q//10
k=n*n
l=math.pow(10,c)
if k%l==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")