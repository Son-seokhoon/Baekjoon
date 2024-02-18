a=int(input())
b=list(input().split())
c=0
d=0
for i in range(a):
    if b[i]=="1":
        c+=1
    if b[i]=="0" or i==(a-1):
        if c==1:
            d+=1
            c=0
        else:
            d+=((c*(c+1))//2)
            c=0
print(d)
