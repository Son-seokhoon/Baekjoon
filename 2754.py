score=input()
a=4.0
b=3.0
c=2.0
d=1.0
f=0.0
if score[0]=="A":
    if score[1]=="+":
        print(a+0.3)
    elif score[1]=="0":
        print(a)
    else:
        print(a-0.3)
elif score[0]=="B":
    if score[1]=="+":
        print(b+0.3)
    elif score[1]=="0":
        print(b)
    else:
        print(b-0.3)
elif score[0]=="C":
    if score[1]=="+":
        print(c+0.3)
    elif score[1]=="0":
        print(c)
    else:
        print(c-0.3)
elif score[0]=="D":
    if score[1]=="+":
        print(d+0.3)
    elif score[1]=="0":
        print(d)
    else:
        print(d-0.3)
else:
    print(f)