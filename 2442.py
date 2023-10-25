a=int(input())

for i in range(1,a+1):
    print(" "*((a-2*i-1)//2)+"*"*(2*i-1)+" "*((a-2*i-1)//2))