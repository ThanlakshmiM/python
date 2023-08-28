class node:
  def __init__(self,Data):
    self.data=Data
    self.front=None
    self.next=None

class doubleLinklistHead:
  def __init__(self):
    self.head=None                # data top first is head starting=none node
  def show(self):
     t=self.head
     while t is not None:
          print(t.data)
          t=t.next
  def insertNextMid(self,mid,data):
    newnode=node(data)
    newnode.next=n4.next
    newnode.front=n5.front
    n4.next=newnode
  def __remove_node(self, node):   # node=t
        if node.front is None:             # node ku munnadi none na irukuna    (front)
            self.head = node.next           # node ta front-->none athu head ----> antha node.next ini head
        else:                                # illa na is none irunthal
            node.front.next = node.next       # node ku munnadi irukuravanga next-->node ta next

        if node.next is None:              # node=t (next) ,node ta aduthu none na irunthal
            self.end = node.front          # node da end--->node ku munnadi irukuravanga than ini end
        else:                              # apti illa na  is none na irunthal
            node.next.front = node.front   # node ta next node ta front---> ini node ta front than

  def remove(self,Removedata):
    t=self.head
    while t is not None:
       if t.data==Removedata:
         self.__remove_node(t)
       t=t.next
          

class doubleLinklistEnd:
  def __init__(self):
    self.end=None                # data bottom is end    endind=none node
  def show(self):
     t=self.end
     while t is not None:
          print(t.data)
          t=t.front

  def insertFrontMid(self,mid,data):
    newnode=node(data)
    newnode.front=n5.front
    newnode.next=n4.next
    n5.front=newnode



n1=doubleLinklistHead()
n6=doubleLinklistEnd()

n1.head=node("thivya")
n6.end=node("thanam")

n2=node("murugan")
n3=node("kavitha")
n4=node("sutha")
n5=node("prema")

n1.head.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6.end
n2.front=n1.head
n3.front=n1.head.next
n4.front=n2.next
n5.front=n3.next
n6.end.front=n4.next

print("-------------double forword conection-------- ")
n1.show()
print("-------------double reverse conection-------- ")
n6.show()
print("-------------forword add middle-------- ")
n1.insertNextMid(n4,"kaviya")
n1.show()
print("-------------reverse add middle-------- ")
n6.insertFrontMid(n4,"kaviya")
n6.show()
print("-------------forword remove middle-------- ")
n1.remove("sutha")
n1.show()
print("-------------forword remove middle(head)-------- ")
n1.remove("thivya")
n1.show()
print("-------------forword remove middle(head)-------- ")
n1.remove("thanam")
n1.show()
print("-------------forword remove middle(head)(unknow data)-------- ")
n1.remove("kayal")
n1.show()

