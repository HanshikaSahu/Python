# remove loops if any

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


  def createLoops(self):
    if self.head is None or self.head.next is None:
      return
    last = self.head
    while last.next is not None:
      last = last.next
    last.next = self.head.next


  def removeLoops(self):
    if self.head is None or self.head.next is None:
      return
    slow = fast = self.head
    while slow and fast and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        slow = self.head
        while slow != fast:
          slow = slow.next
          fast = fast.next
        while fast.next != slow:
          fast = fast.next
        fast.next = None


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(40)
LL1.insert(60)
LL1.createLoops()
LL1.removeLoops()
LL1.printList() 