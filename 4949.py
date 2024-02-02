while True:
    a=input()
    if a==".":
        break
    b=[]
    c=""
    flag=0
    for i in range(len(a)):
        if a[i]=="(" or a[i]=="[":
            b.append(a[i])
        elif a[i]==")":
            if b==[]:
                print("no")
                flag+=1
                break
            c=b.pop()
            if c!="(":
                print("no")
                flag+=1
                break
        elif a[i]=="]":
            if b==[]:
                print("no")
                flag+=1
                break
            c=b.pop()
            if c!="[":
                print("no")
                flag+=1
                break

    if b!=[]:
        if flag == 0:
            print("no")
    elif flag==0:
        print("yes")
