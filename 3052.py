a=[]
for i in range(10):
    b=int(input())
    a.append(b%42)
a=list(set(a))
print(len(a))