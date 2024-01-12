a=int(input())
b=[]
c=[]
while True:
    if a==0:
        print(len(c))
        break
    for i in range(7):
        b.append(a-2**i)
        b.sort()
    for i in range(len(b)):
        if b[i]>=0:
            c.append(2**(6-i))
            a=b[i]
            b=[]
            break
