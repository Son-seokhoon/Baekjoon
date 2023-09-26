a = int(input())
b = 1
while True:
    a = a-b
    b = b+1
    if a < 0:
        print(b-2)
        break