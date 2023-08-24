Name=input("Enter the name ")
AccNo=int(input("Enter the AccNo "))
TotalAmount=int(input("Enter the TotalAmount "))
Debited=int(input("Enter the DebitedAmount "))
AvlBal=TotalAmount-Debited
BankName=input("Enter the Bankname ")
import pytz
import datetime
DateTime=pytz.timezone("asia/kolkata")
ctime=datetime.datetime.now(DateTime)
statement="hi {} !, A/c* {} \ncredited for Rs.{} on {} .\nAvl bal Rs:{}-{}"
print(statement.format(Name,AccNo,Debited,ctime,AvlBal,BankName))