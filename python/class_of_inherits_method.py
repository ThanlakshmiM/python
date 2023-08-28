class emp:# parant
  def __init__(self,ID,Name,Salary,Loc,Dob,Gender,Doj,Exp,Mobile,Address,Aadhar,Bloodgroup):
    self.id=ID
    self.name=Name
    self.salary=Salary
    self.loc=Loc
    self.dob=Dob
    self.gender=Gender
    self.doj=Doj
    self.exp=Exp
    self.mobile=Mobile
    self.address=Address
    self.aadhar=Aadhar
    self.bloodgroup=Bloodgroup



class TCS(emp):
  def show(self):
    print("i am ",self.name, "\nmy id is TCS" +str(self.id), "\nmy salary is ",float(round(self.salary,2)),"\nmy loacation is ",self.loc,"\nmy dob" ,self.dob)

class HCL(emp):  # inherits ddd
  def show(self):
    a=self.name.split()
    print("my first name",a[0],"\nmy last name",a[1], "\nMy id is HCL" +str(self.id), "\nMy salary is ",self.salary-(0.1*self.salary),"\ngender ",self.gender,"\nmy bloodgroup",self.bloodgroup,"\ndate of joining",self.doj)


class Infy(emp):
  def show(self):
    print("I Am ",self.name, "\nMy Id Is Infy" +str(self.id), "\nMy annual Salary Is ",self.salary*12,"\nmy exp",self.exp,"\nmy mobile",self.mobile,"\nmy address is",self.address,"\nmy aadhar is",self.aadhar)



  def hike_salary(self):
    self.salary=self.salary+(0.05*self.salary)

w=emp(123,"thanam",50000,"siruseri,chennai","04-04-2002","female","jun 22","4 year",8679867678,"30A,kalany street","1234 5678 8908","+B")
x=HCL(456,"priya m",80000,"siruseri,chennai","04-04-2002","female","jun 27","4 year",8679867678,"30A,kalani street","1234 8966 8908","+B")
y=TCS(678,"thanam",60000,"tharamani,chennai","18-06-2002","female","jun 8","4 year",855767887,"30A,kalai street","1234 1232 8908","+O")
z=Infy(976,"kavi",60000,"kottai,chennai","07-08-2002","female","jun 20","4 year",69776454,"30A,kovil street","1234 5672 3908","+A")

x.show()
y.show()
z.show()