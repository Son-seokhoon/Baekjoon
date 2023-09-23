a,b,c=map(int,input().split())
d=int(input())
c = d + c
if c >= 60:
    b = b + c//60
    c = c%60
if b >= 60:
    a = a + b//60
    b = b%60
a%=24
print(f"{a} {b} {c}")
