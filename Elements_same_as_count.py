n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if i not in s:
        s.append(i)
b=[]
for j in s:
    if a.count(j)==j:
        b.append(j)
if len(b)>0:
    print(*b)
else:
    print('-1')
        