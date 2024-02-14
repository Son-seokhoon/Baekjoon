a=0
b=[]
for i in range(7):
    c=int(input())
    if c%2==1:
        b.append(c)
        a+=c
if b==[]:
    print(-1)
else:
    b.sort()
    print(a)
    print(b[0])