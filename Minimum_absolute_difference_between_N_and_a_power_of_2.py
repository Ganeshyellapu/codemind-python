n=int(input())
c=0
for i in range(1,n+1):
    if 2**i==n:
        c=0
        print('0')
        break
    elif 2**i>n:
        c=1
        l=2**(i-1)
        m=2**(i)
        break
if c==1:
    if abs(n-l)>abs(m-n):
        print(m-n)
    else:
        print(n-l)