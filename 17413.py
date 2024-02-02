a=input()
b=0
d=[]
a=a+" "
for i in range(len(a)):
    d.append(a[i])
    if a[i]==" " or a[i]=="<":
        if b==1:
            continue
        d.reverse()
        for l in range(len(d)-1):
            print(d[l+1],end="")
        d=[]
        if a[i]=="<":
            d=["<"]
        else:
            print(" ",end="")

    if a[i]=="<" or a[i]==">":
        b+=1
    if b==2:
        for l in range(len(d)):
            print(d[l],end="")
        b=0
        d=[]