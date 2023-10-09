a= input()
if len(a)==1:
        print("1")

for i in range(len(a)//2):
    if a[i]!=a[len(a)-i-1]:
        print("0")
        break
    if i == (len(a)//2)-1:
        print("1")