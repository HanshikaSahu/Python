# find intersection in y-shaped linked list   ##
#(intersection finds same node and not value)

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  

  def printList(self):
    if self.head is None:
      print("Linked list is empty")
    else:
      curr = self.head
      while curr is not None:
        print(curr.data, "-->", end=" ")
        curr = curr.next
      print("None")


  def insert(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = new_node


  def intersection(self, head2):
    ptr1 = self.head
    ptr2 = head2.head
    if ptr1 is None or ptr2 is None:
      return
    while ptr1 != ptr2:
      if ptr1 is not None:
        ptr1 = ptr1.next
      else:
        ptr1 = head2.head
      if ptr2 is not None:
        ptr2 = ptr2.next
      else:
        ptr2 = self.head
    return ptr1
  
LL1 = LinkedList()
LL1.insert(10)
LL1.insert(10)
LL1.insert(40)
LL1.insert(60)  
LL2 = LinkedList()
LL2.insert(30)
LL2.insert(50)
LL2.insert(40) 

temp = LL2.head
while temp.next is not None:
  temp = temp.next
temp.next = LL1.head.next.next.next

intersection_point = LL1.intersection(LL2)  
if intersection_point is None:
  print("-1")
else:
  print(intersection_point.data)