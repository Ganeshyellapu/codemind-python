import math
n=int(input())
for i in range(n):
    a=int(input())
    k=int(math.sqrt(a))
    if a==k*k:
        print("True")
    else:
        print("False")