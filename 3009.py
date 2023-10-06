x=[]
y=[]
for i in range (3):
    a,b=map(int, input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
xpos=0
ypos=0
if x[0] == x[1]:
    xpos=x[2]
else:
    xpos=x[0]
if y[0] == y[1]:
    ypos=y[2]
else:
    ypos=y[0]

print(xpos,ypos)