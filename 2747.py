a=int(input())
b=[0,1]
for i in range(a-1):
    b.append(b[i]+b[i+1])
print(b[a])