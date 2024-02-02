num=int(input())

for i in range(num):
    b=[]
    c=0
    d=0
    a=int(input())
    b=list(map(int,input().split()))
    b.sort()
    print((b[len(b)-1]-b[0])*2)