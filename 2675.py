a = int(input())

for i in range (a):
    b,c = input().split()
    b = int(b)
    d =""
    for i in range (len(c)):
        d += (c[i]*b)
    print(d)
    