a = int(input())
b = int(input())
c=[]
d=0
for i in range(1,101):
    if a <=i*i and i*i <=b:
        c.append(i*i)
for i in range(len(c)):
    d = d+c[i]
c.sort
if d==0:
    print("-1")
else:
    print(d)
    print(c[0])