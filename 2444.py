a=int(input())

for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))
for l in range(a-1,0,-1):
    print(" "*(a-l)+"*"*(2*l-1))