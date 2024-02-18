a=int(input())
b=int(input())
c=int(input())
a=a*b*c
a=str(a)
for i in range(10):
    b=0
    for l in range(len(a)):
        if int(a[l])==i:
            b+=1
    print(b)        
