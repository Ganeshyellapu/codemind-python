a=int(input())
sum=0
pro=1
temp=a
while temp>0:
    r=temp%10
    sum+=r
    pro*=r
    temp=temp//10
if sum==pro:
    print("Spy Number")
else:
    print("Not Spy Number")

