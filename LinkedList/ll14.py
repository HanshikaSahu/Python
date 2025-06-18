# Insertion sort

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


  def insertion(self, head, node):
    if head is None or node.data < head.data:
      node.next = head
      return node
    else:
      curr = head
      while curr.next is not None and curr.next.data < node.data:
        curr = curr.next
      node.next = curr.next
      curr.next = node
      return head
    

  def insertionSort(self):
    sorted_head = None
    curr = self.head
    while curr is not None:
      next_node = curr.next
      sorted_head = self.insertion(sorted_head, curr)
      curr = next_node
    self.head = sorted_head


LL1 = LinkedList()
LL1.insert(20)
LL1.insert(30)
LL1.insert(10)  
LL1.insert(40)  
LL1.insert(50)
LL1.insertionSort()
LL1.printList()