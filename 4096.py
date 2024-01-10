while True:
    a=input()
    c=0
    d=len(a)
    if a=="0":
        break
    while True:
        b=0
        for i in range(len(a)//2):
            if a[i]!=a[len(a)-i-1]:
                break
            b+=1
        if b==len(a)//2:
            print(c)
            break
        c +=1
        a=int(a)+1
        a=str(a)
        a = "0"*(d-len(a))+a
