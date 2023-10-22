a=int(input())
b=[0,1]
for i in range(2,a+1):
    b.append(b[i-2]+b[i-1])
print(b[a])