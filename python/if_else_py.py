a=int(input("enter the amount  "))
if a>1000:
  print("meals,snecks,juice,water")
else:
  if a>500 and a<1000:
    print("meals,snecks")
  else:
    if a>300 and a<500:
      print("meals only")
    else:
      if a>100 and a<300:
        print("snecks only")
      else:
        print(" water only")