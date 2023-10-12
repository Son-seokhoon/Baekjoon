n=int(input())
if n%10 != 0:
    print("-1")
elif n>=300 or n >= 60 or n >=10:
    A=n//300
    n=n%300
    B=n//60
    n=n%60
    C=n//10
    print(A,B,C)