class Node:
  def __init__(self,Data):
    self.data = Data
    self.next = None
class link_list:
  def remove(self,removeData):    #self=N1 , removeData= sri
    temp = self.head
    while temp is not None:
     if temp.data==removeData:
      break
     previousNode = temp       # assign previousNode = temp
     temp = temp.next          ## temp = temp.next ---> moving........loop end


    if temp:
      previousNode.next=temp.next

    else:
        print("----------")
        print('No such Data')
        print("----------")

  def removehead(self,removeData):  # self=N1 , removeData= sofia
    temp = self.head                 # create temp -----> assign self.head=N1.head
    while temp is not None:          # check temp  until the end
     if temp.data==removeData:       #  temp= N1.head condition(1) check N1.head=removeData----> sofia == sofia, True
      self.head=temp.next             # sofia is the head ---> head assign---> next node is head (assign)
      break
     temp = temp.next                # temp = temp.next ---> moving........loop end


    if temp:                            # condition(2) temp
      self.head.next=temp.next.next     # self.head.next=N1.head.next=N2   , temp.next.next=self.head.next.next=N3 , True

    else:
        print("----------")
        print('No such Data')
        print("----------")



  def insertHead(self,new_data):
    tempNode = Node(new_data)      # create tempNode calling based on node class
    tempNode.next = self.head     # assign tempNode.next---->head
    self.head = tempNode          # assign head = temNode


  def insertMid(self,MidNode,new_data):
    tempNode = Node(new_data)           # create tempNode calling based on node class
    tempNode.next = MidNode.next        # assign tempNode.next----> MidNode.next=N4
    MidNode.next = tempNode             # assign MidNode.next----->tempNode

  def insertEnd(self,EndNode,new_data):
       tempNode=Node(new_data)           # create tempNode calling based on node class
       EndNode.next=tempNode             # EndNode=N5---> EndNode.next=tempNode assign

  def __init__(self):
    self.head = None

  def show(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next

N1 = link_list()
N1.head = Node("Murugan")

N2 = Node("Kavitha")
N3 = Node('Thanam')
N4 = Node('Prema')
N5 = Node('Sudha')

N1.head.next = N2
N2.next = N3
N3.next = N4
N4.next = N5

print("-------Before Insert--------")
N1.show()
print("-------After Insert Middle--------")
N1.insertMid(N3,"Abi")
N1.show()
print("-------After Insert Begining--------")
N1.insertHead("Nali Naya")
N1.show()
print("---------After Insert Ending------")
N1.insertEnd(N5,"Karthika")
N1.show()
print("-------After Removing (Known Value)-------")
N1.remove("Thanam") #1 Calls remove function #20 Success for step 1 to 19
N1.show()
print("-------After Removing(Not present)-------")
N1.remove("Priya")
N1.show()
print("-------After Removing (Known Value),Identify the error & solve-------")
N1.removehead("Nali Naya")
N1.show()