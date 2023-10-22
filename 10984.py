num=int(input())

for i in range(num):
    t=int(input())
    a = int(0)
    b = float(0.0)
    for l in range(t):
        x,y=input().split()
        a += int(x)
        b += float(y)*int(x)
    
    print(a,round(b/a,1))