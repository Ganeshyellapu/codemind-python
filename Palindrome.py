n=int(input())
total=0
q=n
while(q!=0):
    r=q%10
    total=total*10+r
    q=q//10
if total==n:
    print('True')
else:
    print('False')