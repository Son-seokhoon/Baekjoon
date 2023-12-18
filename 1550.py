a = input()
a = list(reversed(a))
b=0
for i in range(len(a)):
    if ord(a[i]) > 64:
        b=b+((ord(a[i])-55)*(16**i))
    else:
        b=b+(int(a[i])*(16**i))
print(b)