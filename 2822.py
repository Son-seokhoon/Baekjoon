a=[]
b=[]
x=[]
c=0
for i in range(8):
    a.append(int(input()))
b=list(a)
a.sort()
for i in range(5):
    c+=a[len(a)-i-1]
    x.append(b.index(a[len(a)-i-1])+1)
x.sort()
print(c)
print(x[0],x[1],x[2],x[3],x[4])
