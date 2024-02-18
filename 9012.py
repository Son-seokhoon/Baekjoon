num=int(input())
for i in range(num):
    x=input()
    b=0
    for l in range(len(x)):
        if x[l]=="(":
            b+=1
        elif x[l]==")" and b==0:
            b-=1
            break
        else:
            b-=1
    if b==0:
        print("YES")
    else:
        print("NO")