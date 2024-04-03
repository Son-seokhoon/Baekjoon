a=[]
for i in range(9):
    a.append(int(input()))
a.sort()
for i in range(9):
    for l in range(1,9):
        if l>i:
            if (sum(a)-a[i]-a[l])==100:
                a[i]=0
                a[l]=0
                a.remove(0)
                a.remove(0)
                break
    if len(a)==7:
        break
for i in range(len(a)):
    print(a[i])