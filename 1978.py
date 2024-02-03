def primenum(x):
    if x==1:
        return 0
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
a=int(input())
b=list(map(int,input().split()))
count=0
for i in range(a):
    count+=primenum(b[i])

print(count)