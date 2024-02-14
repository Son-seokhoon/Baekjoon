a=int(input())
for i in range(a):
    b=int(input())
    print(f"Pairs for {b}:",end="")
    for l in range(1,(b//2)+1):
        if l==(b-l):
            break
        elif l>1:
            print(",",end="")
        print(f" {l}",end="")
        print(f" {b-l}",end="")
    print()