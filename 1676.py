a=int(input())
b=1
for i in range(1,a+1):
    b*=i
b=str(b)[::-1]
for i in range(len(b)):
    if b[i]!="0":
        print(i)
        break