n=list(map(str,input().split()))
a='aeiouAEIOU'
b=[]
for i in n:
    t=i
    c=0
    for j in range(len(t)):
        if t[j] in a:
            c+=1
    b.append(c)
v=max(b)
s=0
for i in b:
    if i==v:
        s+=1
print(s)