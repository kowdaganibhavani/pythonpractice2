import random
a=[{
    "name":"jenny",
    "follower":6,
    "profession":"lecture",
    "country":"india"
},{
    "name":"virat",
"follower": 456,
"profession": "criker",
"country": "landon"
},
    {
"name":"critan",
    "follower":786,
    "profession":"vollybal",
    "country":"austraila"
    },{
"name":"kajol",
    "follower":66,
    "profession":"actor",
    "country":"india"
    }]
"""f1=random.choice(a)
f2=random.choice(a)
name=f1["name"]
pro=f1["profession"]
con=f1["country"]
print(f"{name} and {pro} from {con}")
name2=f2["name"]
pro2=f2["profession"]
con2=f2["country"]
print(f"{name2} and {pro2} from {con2}")
inp=int(input("enter 1 or 2"))
foll1=f1["follower"]
foll2=f2["foll"""

def fun(guess,foll,follo):
    if foll<follo:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return  False
nin=False
while not nin:
    f1 = random.choice(a)
    f2 = random.choice(a)
    name = f1["name"]
    pro = f1["profession"]
    con = f1["country"]
    print(f"{name} and {pro} from {con}")
    name2 = f2["name"]
    pro2 = f2["profession"]
    con2 = f2["country"]
    print(f"{name2} and {pro2} from {con2}")
    inp = int(input("enter 1 or 2"))
    foll1 = f1["follower"]
    foll2 = f2["follower"]
    p = 0
    guess = int(input("type 1 or 2"))
    gu = fun(guess, foll1, foll2)
    if gu:
        p += 1
        print(f"ur write ur scoreis {p}")
    else:
        nin=True
        print(f"ur score {p}")