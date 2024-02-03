def primenum(x):
    if x==1:
        return 0
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=[]
d=0
for i in range(a,b+1):
    if primenum(i)==1:
        c.append(i)
if c==[]:
    print("-1")
else:
    c.sort()
    for i in range(len(c)):
        d+=c[i]
    print(d)
    print(c[0])
