num=int(input())
money=[]
for i in range(num):
    a=list(map(int, input().split()))
    a.sort()
    if a[0]==a[1]==a[2]:
        money.append(10000+a[0]*1000)
    elif a[0]==a[1] or a[1]==a[2]:
        money.append(1000+a[1]*100)
    else:
        money.append(a[2]*100)
money.sort(reverse=True)
print(money[0])
