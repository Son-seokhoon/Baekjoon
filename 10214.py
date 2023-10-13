num=int(input())

for i in range(num):
    Y=0
    K=0
    for i in range(9):
        a,b=map(int,input().split())
        Y=a+Y
        K=b+K
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")