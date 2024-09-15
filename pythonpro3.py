import random
print("let me think numbers between 1 to 30")
inp=input("select the level its hard or easy")
val=int(input("entr number"))
com=random.randint(1,50)
print(com)
a=10
inn=True
while inn:
 if inp=="easy":

  if com>val:
      print("its low")
  elif com<val:
      print("its high")

  print(f"no of attempts is {a}")
  a -= 1
  val = int(input("entr number"))

  if a<0:
    inn=False
    print("bye")
  if com==val:
      print("ur guess correct")
      inn=False