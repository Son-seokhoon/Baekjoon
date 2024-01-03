a=int(input())

for i in range(a):
    if i%2==0:
        for i in range(a):
            print("* ",end="")
        print("")        
    else:
        for i in range(a):
            print(" *",end="")
        print("")