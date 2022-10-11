import math
n=int(input())
s=math.sqrt(n)
if(s*s==n and n%s==0):
    print(True)
else:
    print(False)