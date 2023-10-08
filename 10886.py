n = int(input())
c=0
for i in range(n):
    a=input()
    if a=="1":
        c=c+1
    else:
        c=c-1
if c >= 1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")