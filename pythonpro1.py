print("start quiz game")
a=[{"text":"what is the full form of ATM","answer":"A"},
   {"text":"what is flower","answer":"B"},{"text":"what is fruit","answer":"A"},
   {"text":"what is vegetable","answer":"A"}]
opt=[["A.automatic transfer machine","B.auto tran machi","C.both A and B","D.none of the above"],
     ["A.apple","B.rose","c.jackfruit","D.NONE"],["A.papu","B.APPLE","C.oil","D.NONE"],
     ["A.spinach","B.kakarkaya","c.ntg","D.NONE"]]
score=0
def check(guessing,corr):
    if guessing==corr:
        return True
    else:
        return False
for i in range(len(a)):
    print(a[i]["text"])
    for j in opt[i]:
        print(j)
    u=input("enter ur answeA/B/C/D")
    h=check(u,a[i]["answer"])
    if h:
        score+=1
        print("correcr")

    else:
        print("incorrect")
        print(f"the correct ans{a[i]['answer']}")
    print(f"{score}/{i+1}")
print(f"{(score/len(a))*100}")