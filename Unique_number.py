n=int(input())
q=n
a=[]
while(q):
    r=q%10
    a.append(r)
    q=q//10
for i in a:
    if a.count(i)>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")