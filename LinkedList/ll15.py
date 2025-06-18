# rotate double linked list by n nodes
#(done by making it circular and then break it)

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    if self.head is None:
      print("Linked list is empty")
    else:
      curr = self.head
      while curr is not None:
          if curr.next is None:
            print(curr.data, end=" ")
          else:
            print(curr.data, "<-->", end=" ")
          curr = curr.next


  def insert(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = new_node
      new_node.prev = curr


  def rotateDLL(self, n):
    tail = self.head
    while tail.next is not None:
      tail = tail.next
    tail.next = self.head
    self.head.prev = tail
    for i in range(n):
      self.head = self.head.next
      tail = tail.next
    tail.next = None
    self.head.prev = None


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(70)
LL1.insert(50)
LL1.insert(40)
LL1.insert(60)
LL1.insert(30)
LL1.rotateDLL(2)
LL1.printList()