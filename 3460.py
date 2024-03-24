num=int(input())
for i in range(num):
    x=int(input())
    x=str(bin(x)[::-1])
    for l in range(len(x)):
        if x[l]=="1":
            print(l,end=" ")