while True:
    n=int(input())
    f=[]
    p=0
    if n == -1:
        break
    for i in range(1,n):
        if n%i==0:
            f.append(i)
    for i in range(len(f)):
        p=p+f[i]
    if p == n:
        print(n,"= 1",end="")
        for i in range(1,len(f)):
            print(" +",f[i],end="")
        print()
    else:
        print(n,"is NOT perfect.")