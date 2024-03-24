a=int(input())
b=list(map(int,input().split()))
num=int(input())
for i in range(num):
    x,y=map(int,input().split())
    if x==1:
        for l in range(1,a//y+1):
            if b[y*l-1]==0:
                b[y*l-1]=1
            elif b[y*l-1]==1:
                b[y*l-1]=0
    else:
        c=[]
        c.append(y-1)
        c.append(a-y)
        c.sort()
        y-=1
        if c[0]==0:
            if b[y]==1:
                b[y]=0
            else:
                b[y]=1
        else:
            for l in range(c[0]+1):
                if b[y-l]!=b[y+l]:
                    break
                else:
                    if b[y-l]==1 and b[y+l]==1:
                        b[y-l]=0
                        b[y+l]=0
                    elif b[y-l]==1 and b[y+l]==0:
                        b[y-l]=0
                        b[y+l]=1
                    elif b[y-l]==0 and b[y+l]==1:
                        b[y-l]=1
                        b[y+l]=0
                    elif b[y-l]==0 and b[y+l]==0:
                        b[y-l]=1
                        b[y+l]=1
num=1
for i in range(1,a+1):
    if (i-(20*num))==1:
        num+=1
        print()
    print(b[i-1],end=" ")