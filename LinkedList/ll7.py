# intersection of sorted linked list

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


  def sortedIntersect(self, ll2):
    ptr1 = self.head
    ptr2 = ll2.head
    tail = None
    result = LinkedList()
    while ptr1 is not None and ptr2 is not None:
      if ptr1.data == ptr2.data:
        if tail is None or tail.data != ptr1.data:
          next_node = Node(ptr1.data)
          if result.head is None:
            result.head = next_node
            tail = next_node
          else:
            tail.next = next_node
            tail = tail.next
        ptr1 = ptr1.next
        ptr2 = ptr2.next
      elif ptr1.data < ptr2.data:
        ptr1 = ptr1.next
      else:
        ptr2 = ptr2.next
    return result


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(40)
LL1.insert(70)
LL2 = LinkedList()
LL2.insert(30)
LL2.insert(40)
LL2.insert(70) 
intersection = LL1.sortedIntersect(LL2)
intersection.printList()