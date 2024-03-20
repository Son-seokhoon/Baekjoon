a,b,c=map(int,input().split())
truck=list(map(int,input().split()))
bridge=[0]*b
time=0
while True:
    if sum(bridge)==0 and sum(truck)==0:
        break
    if bridge[0]!=0 and (sum(bridge[1:])+truck[0]) <= c:
        bridge.append(truck.pop(0))
        truck.append(0)
        bridge.pop(0)
        time+=1
    elif bridge[0]!=0 and (sum(bridge[1:])+truck[0]) > c:
        bridge.append(0)
        bridge.pop(0)
        time+=1
    elif (sum(bridge)+truck[0]) <= c and bridge[0]==0:
        bridge.append(truck.pop(0))
        truck.append(0)
        bridge.pop(0)
        time+=1
    elif (sum(bridge)+truck[0]) > c and bridge[0]==0:
        for i in range(b):
            if bridge[0]!=0:
                break
            bridge.append(0)
            bridge.pop(0)
            time+=1
print(time)