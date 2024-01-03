a=int(input())

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for l in range(i):
        print("* ",end="")
    print()