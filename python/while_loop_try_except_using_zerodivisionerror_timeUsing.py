i=3
while i:
  print("only",i,"time")
  try:
    a=int(input("enter the a value: "))
    b=int(input("enter the b value: "))
    print(a/b)
    break                                  # no error time exit loop use break
  except ZeroDivisionError:
    print("invalid number")
  finally :
     i=i-1