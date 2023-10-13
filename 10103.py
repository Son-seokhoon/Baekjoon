num=int(input())
a=100
b=100
for i in range(num):
    x,y=map(int,input().split())
    if x > y:
        b = b-x
    elif x < y:
        a = a-y
print(a)
print(b)