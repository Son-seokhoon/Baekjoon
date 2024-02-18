a=""
b=0
c=""
while True:
    try:
        a+=input()
    except:
        break
print(sum(map(int, a.split(','))))