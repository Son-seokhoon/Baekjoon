import sys
num=int(sys.stdin.readline())
a=[0]*10001
for i in range(num):
    b=int(sys.stdin.readline())
    a[b]+=1
for i in range(len(a)):
    for l in range(a[i]):
        sys.stdout.write(str(i)+'\n')