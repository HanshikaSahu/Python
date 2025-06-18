# remove duplicates from unsorted double linked list

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


  def remove_duplicates(self):
    hash_set = set()
    curr = self.head
    while curr is not None:
      if curr.data in hash_set:
        if curr.prev is not None:
          curr.prev.next = curr.next
        if curr.next is not None:
          curr.next.prev = curr.prev
        temp = curr
        curr = curr.next
        del temp
      else:
        hash_set.add(curr.data)
        curr = curr.next


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(20)
LL1.insert(50)
LL1.insert(40)
LL1.insert(40)
LL1.insert(30)
LL1.remove_duplicates()
LL1.printList()