case=int(input())
for i in range(case):
    a = list(map(int, input().split()))
    a.sort()
    print(a[7])