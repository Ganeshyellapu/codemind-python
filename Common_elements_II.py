a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in c:
    if i not in d:
        e.append(i)
for j in d:
    if j not in c:
        e.append(j)
print(*e)