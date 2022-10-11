n=int(input())
a=list(map(int,input().split()))
ei=0
oi=0
for i in range(len(a)):
    if i%2==0:
        ei=ei+a[i]
    else:
        oi=oi+a[i]
print(abs(ei-oi))