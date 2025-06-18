# single to circular

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
        if curr == self.head:
          break


  def insert(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


  def circular(self):
    curr = self.head
    while curr.next is not None:
      curr = curr.next
    curr.next = self.head
    return self.head

LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(30)
LL1.circular()
LL1.printList()