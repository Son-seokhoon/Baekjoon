a=0
b=[]
for i in range(5):
    b.append(int(input()))
    a+=b[i]
b.sort()
print(a//5)
print(b[2])