while True:
    a=list(map(int,input().split()))
    if a[0]*a[1]==0:
        break
    if a[0] > a[1]:
        print("Yes")
    elif a[0] <= a[1]:
        print("No")
