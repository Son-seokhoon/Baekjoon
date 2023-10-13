num=int(input())

for i in range(num):
    univ=int(input())
    a=[]
    b=[]
    for l in range(univ):
        x,y=input().split()
        a.append(x)
        a.append(int(y))
        b.append(int(y))
    b.sort(reverse=True)
    for g in range(len(a)):
        if a[g]==b[0]:
            print(a[g-1])
