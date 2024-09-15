import random
le=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
nu=["1","2","3","4","5","6","7","8","9","0"]
sy=["!","@","#","%","%","^","&","*","(",")","-","+","="]
a=int(input("enter letters"))
b=int(input("enter num"))
c=int(input("enter symbols"))
k=[]
for i in range(1,a+1):
    k+=random.choice(le)
for i in range(1,c+1):
    k+=random.choice(sy)
for i in range(1,b+1):
    k+=random.choice(nu)
random.shuffle(k)
s=""
for i in p:
    s+=i
    print(s)