a,b=input().split()
x=""
y=""
for i in reversed(range(3)):
    x+=a[i]
    y+=b[i]
x=int(x)
y=int(y)
print(max(x,y))