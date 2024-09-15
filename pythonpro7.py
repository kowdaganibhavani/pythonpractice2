import random
a=["apple","bananna","sunflower","goodday"]
p=random.choice(a)
print(p)
t=["""----------
          |       
          0
         / \ 
         / \ ""","""---------
                        |
                        0   
                        / \ 
                        /""",
                 """---------
                                         |
                                         0   
                                         / \ 
                                         ""","""---------
                        |
                        0   
                        / 
                        ""","""---------
                        |
                        0   
                        
                ""","""---------
                        |
                    """
   ]
x=[]
c=6
gover=False
for i in range(len(p)):
    x += "_"
print(x)
#inp = input("enter input")

while not gover:
    inp = input("enter input")
    for j in range(len(p)):
        lete= p[j]
        if lete == inp:
            x[j] = inp
    print(x)
    if inp not in p:
        c -= 1
        if c < 0:
            gover = True
            print(" you loss")

    if "_" not in x:
        gover=True
        print("win")
    print(t[c])
