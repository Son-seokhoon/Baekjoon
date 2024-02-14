a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(len(b)):
    if a==b[i]:
        c+=1
print(c)