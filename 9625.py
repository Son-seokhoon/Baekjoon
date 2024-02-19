num=int(input())
x=[[1,0],[0,1]]
if num>1:
    for i in range(2,num+1):
        a=(x[i-1][1])
        b=(x[i-1][0]+x[i-1][1])
        x.append([a,b])
print(x[num][0],x[num][1])