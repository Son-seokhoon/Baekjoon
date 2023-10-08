n=int(input())
z=input()
A=0
B=0
for i in range(n):
    if z[i]=="A":
        A=A+1
    else:
        B=B+1
if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")