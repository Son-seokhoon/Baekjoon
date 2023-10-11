a=int(input())

for n in range(a):
    b=0
    c=0
    ox=input()
    for i in range(len(ox)):
        if ox[i] =="O":
            c=c+1
        else:
            b=b+c*(c+1)//2
            c=0
    b=b+c*(c+1)//2
    print(b)