b={}
for i in range(1,6):
    a=list(map(int,input().split()))
    b[i]=sum(a) 
c=[]
c=list(b.values())
c.sort(reverse=True)
d=dict(map(reversed,b.items()))
print(d[c[0]],c[0])