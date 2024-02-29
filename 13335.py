a,b,c=map(int,input().split())
car=list(map(int,input().split()))
bridge=[0]*b
num=0
time=0
for i in range(len(car)):
    if num>i:
        continue
    bridge.pop(0)
    bridge.append(car[i])
    num+=1
    for l in range(i,len(car)):
        if l==(len(car)-1):
            bridge.pop(0)
            bridge.append(car[l])
            time+=1
            num+=1
            if sum(bridge)>c:
                bridge.pop()
                bridge.append(0)
                num-=1  
        elif l!=(len(car)-1):
            bridge.pop(0)
            bridge.append(car[l+1])
            time+=1
            num+=1
            if sum(bridge)>c:
                bridge.pop()
                bridge.append(0)
                num-=1
                break
    while bridge[0]==0:
        bridge.pop(0)
        bridge.append(0)
        time+=1
while sum(bridge)!=0:
    bridge.pop(0)
    bridge.append(0)
    time+=1
print(bridge)
print(time)
