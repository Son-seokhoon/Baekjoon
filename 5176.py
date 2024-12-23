case=int(input())
for i in range(case):
    a,b=map(int,(input().split()))
    c=[int(input()) for _ in range(a)]
    c=list(set(c))
    print(a-len(c))
