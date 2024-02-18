num=0
x=[]
for i in range(4):
    a,b=map(int,input().split())
    num+=b
    num-=a
    x.append(num)
x.sort(reverse=True)
print(x[0])
