num = int(input())
people={}
for i in range(num):
    n,d,m,y=input().split()
    age=0
    age = (int(y)*12+int(m))*31+int(d)
    people[age]=n
age=sorted(people.keys())
print(people[age[len(age)-1]],"\n"+people[age[0]])