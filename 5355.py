a = int(input())

for i in range(0, a):
    b = input().split()
    c = float(b[0])
    for i in range(1,len(b)):
        if b[i] == "@":
            c = c*3
        elif b[i] == "%":
            c = c+5
        elif b[i] == "#":
            c = c-7
    print("{:.2f}".format(c))


