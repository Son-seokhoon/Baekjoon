a=int(input())

for i in range(1,a+1):
    for l in range(a-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()