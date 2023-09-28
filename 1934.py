def gdc(x, y):
    while y > 0:
        x, y = y, x % y
    return x
def lcm(x, y):
    return x * y // gdc(x, y)

a = int(input())
for i in range(a):
    b,c=map(int,input().split())
    print(lcm(b, c))
    
