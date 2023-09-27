a = int(input())
for i in range(a):
    b,c=map(int,input().split())
    l = []
    for i in range(1,c+1):
        l.append(b*i)
    for i in range(1,b+1):
        d = c*i
        if d in l:
            print(d)
            break
        