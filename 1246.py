a,b=map(int,input().split())
c=[]
d=[]
x=0
y=0
for i in range(b):
    c.append(int(input()))
c.sort()
for i in range(b):
    if a>(b-i) and y<(c[i]*(b-i)):
        x=c[i]
        y=(c[i]*(b-i))
    elif a<=(b-i) and y<(c[i]*a):
        x=c[i]
        y=c[i]*a
print(x,y)
