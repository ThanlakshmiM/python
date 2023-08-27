a=["murugan","kavitha","suthadevi","prema","thanalakshmi","karthika"]
search=input("enter the name: ")
c=0
for i in a:
  c=c+1
  if i==search:           # value & index both print
        print(i)
        break
  else:
      if c==6:
        print("no such a data")