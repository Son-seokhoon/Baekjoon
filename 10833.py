num=int(input())
c=0
for i in range(num):
    a,b=map(int,input().split())
    c=c+b-a*(b//a)
print(c)