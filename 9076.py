case=int(input())
for i in range(case):
    x=[]
    y=0
    x=list(map(int,input().split()))
    x.sort()
    if x[3]-x[1]>=4:
        print("KIN")
    elif x[3]-x[1]<4:
        y+=x[1]
        y+=x[2]
        y+=x[3]
        print(y)


