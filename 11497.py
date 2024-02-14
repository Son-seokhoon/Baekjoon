a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=[]
    e=[]
    c.sort()
    for l in range(b):
        if l%2==0:
            d.append(c[l])
    for l in range(b-1,0,-1):
        if l%2==1:
            d.append(c[l])
    for l in range(b-1):
        e.append(abs(d[l+1]-d[l]))
    e.append(abs(d[b-1]-d[0]))
    e.sort(reverse=True)
    print(e[0])