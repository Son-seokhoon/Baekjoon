a,b,c=map(int,input().split())
if a%(c-b)==0:
    print(a//((c-b)))
else:
    print(a//(c-b)+1)