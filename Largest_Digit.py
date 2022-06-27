n=int(input())
add=n%10
while n!=0:
    r=n%10
    if add<r:
        add=r
    n=n//10
print(add)