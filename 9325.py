a=int(input())

for i in range(a):
    car=int(input())
    b=int(input())
    for l in range(b):
        x,y=map(int,input().split())
        car=car+x*y
    print(car)
    