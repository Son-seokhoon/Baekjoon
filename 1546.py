a=int(input())
b=list(map(int,input().split()))
c=[]
b.sort(reverse=True)
for i in range(1,a):
    c.append(b[i]/b[0]*100)
c.append(100)
print(sum(c)/len(c))