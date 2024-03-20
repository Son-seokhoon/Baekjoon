a,b=map(int,input().split())
c=[]
for i in range(1,b+1):
    if len(c)==b:
        break
    for l in range(i):
        if len(c)==b:
            break
        c.append(i)
print(sum(c[(a-1):(b)]))