a={1:"murugan",2:"kavitha",3:"suthadevi",4:"prema",5:"thanalakshmi",6:"karthika"}
key=int(input("enter the key: "))
value=input("enter the value: ")
b=a.get(key)
if b==value:
  print("verify credentials based on username password  match ")
else:
  print("verify credentials based on username password not match ")
