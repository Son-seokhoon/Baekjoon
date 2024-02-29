import sys
num=int(input())
a=[0]*10001
b=0
for i in range(num):
    b=int(sys.stdin.readline())
    a[b]+=1
for i in range(len(a)):
    for l in range(a[i]):
        sys.stdout.write(str(i)+'\n')