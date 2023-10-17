a=list(map(int,input().split(":")))
b=list(map(int,input().split(":")))

h = b[0]-a[0]
m = b[1]-a[1]
s = b[2]-a[2]

if s < 0:
    m = m-1
    s = s+60
if m < 0:
    h = h-1
    m = m+60
if h < 0:
    h = h+24
if h < 10:
    h="0"+str(h)
if m < 10:
    m="0"+str(m)
if s < 10:
    s="0"+str(s)

print(f"{h}:{m}:{s}")