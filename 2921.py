a=int(input())
b=0
for i in range(1,a+1):
    b=b+(((2*i+i)*(2*i-i+1))//2)
print(b)