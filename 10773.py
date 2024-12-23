num=int(input())
a=[]
b=0
for i in range(num):
    b=int(input())
    if b ==0:
        a.pop()
    else:
        a.append(b)
print(sum(a))