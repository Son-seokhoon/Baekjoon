a,b=map(int, input().split())

b = b-45

if b < 0:
    a = a-1
    b = b+60
    if a < 0:
        a=23
print(a,b)