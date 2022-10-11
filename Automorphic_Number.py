n=input()
k=len(n)
n=int(n)
if n<0:
    n=n*-1
m=n*n
if m%(10**k)==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")