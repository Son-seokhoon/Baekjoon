a,b=map(int,input().split())
x,y=map(int,input().split())
if x+y<a:
    print("IMPOSSIBLE")
elif x-y>b:
    print("IMPOSSIBLE")
elif x+y<b and x-y>a:
    print(y*2+1)
elif x+y<b and x-y<a:
    print(x+y-a+1)
elif x+y>b and x-y>a:
    print(b-(x-y)+1)
elif x+y>b and x-y<a:
    print(b-a+1)
else:
    print("IMPOSSIBLE")