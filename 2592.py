y=[]
z=[]
result=[]
for i in range(10):
    x=int(input())
    y.append(x)
y.sort()
print(sum(y)//10)
z=list(set(y))
for i in range(len(z)):
    result.append(y.count(z[i]))
for i in range(len(result)):
    if result[i]==max(result):
        print(z[i])