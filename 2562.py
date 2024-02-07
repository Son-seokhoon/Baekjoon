x=0
y=0
for i in range(9):
    num=int(input())
    if num>x:
        x=num
        y=i+1
print(x)
print(y)