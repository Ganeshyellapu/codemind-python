n=int(input())
'''s1=0
s=0
q=n
sq=n*n
if(n==0):
    print("True")

while sq!=0:
    r=sq%10
    s=s*10+r #441
    sq=sq//10 
    
while q!=0:
    r1=q%10
    s1=s1*10+r1 #21
    q=q//10
if(s==s1*s1):
    print("True")
else:
    print("False")'''
q=str(n)
r=q[::-1] #21
s1=n*n
s2=int(r)*int(r) #441
p=str(s2)
u=p[::-1]
if(int(u)==s1):
    print(True)
else:
    print(False)