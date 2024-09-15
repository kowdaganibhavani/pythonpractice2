import random
t="""-------
----------
------------"""
r="---------"
s="66666666"
p=[t,r,s]
u=int(input("enter 0 for rock,1 for paper,2 for scissor"))
if u>=3 or u<=0:
    print("printed invallid")
else:
    print(p[u])
    c=random.randint(0,2)
    print("computer choice")
    print(p[c])
    if c == u:
        print("dron")
    elif (u == 0 and c == 2):
        print("u win")
    elif (c == 0 and u == 2):
        print("u loss")
    elif (u > c):
        print("u win")
    elif (c > u):
        print("u loss")