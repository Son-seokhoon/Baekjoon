a=int(input())
b=list(map(int,input().split()))
b.sort()
print(b[0],b[len(b)-1])