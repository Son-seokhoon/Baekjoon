num=int(input())

for i in range(num):
    a,b=input().split()
    c=""
    for l in range(len(b)):
        if l==int(a)-1:
            continue
        else:
            c+=b[l]
    print(c)