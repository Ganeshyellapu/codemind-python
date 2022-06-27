n=input()
t=len(n)
c=0
a='aeiouAEIOU'
for i,j in zip(range(t//2),range(t-1,t//2-1,-1)):
    if(n[i]!=' ' and n[j]!=' '):
        if (n[i] in a and n[j] not in a) or (n[i] not in a and n[j] in a):
           c+=1
print(c)