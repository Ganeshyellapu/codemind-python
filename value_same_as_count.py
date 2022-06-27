n=int(input())
a=list(map(int,input().split()))
s=[]
c=0
for i in a:
    if i not in s:
        s.append(i)
for j in s:
    if a.count(j)==j:
        c=c+1
print(c)