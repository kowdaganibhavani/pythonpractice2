def fun(ju):
    k=0
    o=""
    for i in ju:
        p=s[i]
        if p>k:
            o=i
            k=p
    print(k,o)
t=False
while not t:
      s = {}
      name = input("enter name")
      price = int(input("enter salary"))
      s[name] = price
      u = input("enter yes or no")
      if u == "no":
          t = True
          fun(s)