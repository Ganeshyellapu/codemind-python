n=list(map(str,input().split()))
c=0
a='aeiouAEIOU'
for k in n:
    m=k
    t=len(m)
    for i,j in zip(range(t//2),range(t-1,t//2-1,-1)):
        if(m[i]!=' ' and m[j]!=' '):
            if (m[i] in a and m[j] not in a) or (m[i] not in a and m[j] in a):
               c+=1
print(c)