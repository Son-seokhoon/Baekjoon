a=input()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
b.sort(reverse=True)
for i in range(len(b)):
    print(b[i],end="")