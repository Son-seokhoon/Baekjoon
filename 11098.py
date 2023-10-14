a = int(input())
for i in range(a):
    b = int(input())
    z={}
    money=[]
    for l in range(b):
        x,y=input().split()
        z[int(x)]=y
    money=sorted(z.keys(), reverse=True)
    print(z[money[0]])