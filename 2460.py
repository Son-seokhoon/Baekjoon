x=0
y=[]
for i in range(10):
    a,b=map(int,input().split())
    x+=b
    x-=a
    y.append(x)
print(max(y))