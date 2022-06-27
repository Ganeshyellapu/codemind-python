def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return 0
    return 1
n=int(input())
while n:
    k=int(input())
    i,j=0,-1
    while(k):
        if is_prime(k+i):
            t1=k+i
            break
        i+=1
    while(k):
        if is_prime(k+j):
            t2=k+j
            break
        j-=1
    #print(k,t1,t2)
    if t1-k>=k-t2:
        print(t2)
    else:
        print(t1)
    n-=1