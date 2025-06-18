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


  def printList_reverse(self):
    print()                    #to print in next line
    if self.head is None:
      print("Linked list is empty")
      return
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
        
      while curr is not None:
        if curr.prev is None:
          print(curr.data, end= " ")
        else:
          print(curr.data, "<-->" ,end=" ")
        curr = curr.prev


  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node


  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = new_node
      new_node.prev = curr


  def insert_after_node(self, data, target):
    if self.head is None:
      print("List is empty")
      return
    else:
      curr = self.head
      while curr is not None:
        if curr.data == target:
          break
        curr = curr.next
      if curr is None:
        print("node not found")
      else:
        new_node = Node(data)
        new_node.next = curr.next
        new_node.prev = curr
        if new_node.next is not None:
          curr.next.prev = new_node
        curr.next = new_node


  def insert_before_node(self, data, target):
    if self.head is None:
      print("List is empty")
      return
    if self.head.data == target:
      new_node = Node(data)
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
      return
    curr = self.head
    while curr is not None:
      if curr.data == target:
        break
      curr = curr.next
    if curr is None:
      print("node not found")
    else:
      new_node = Node(data)
      new_node.next = curr
      new_node.prev = curr.prev
      if new_node.next is not None:
        curr.prev.next = new_node
      else:
        self.head = new_node
      curr.prev = new_node


  def delete_at_beginning(self):
    if self.head is None:
      print("List is empty")
      return
    if self.head.next is None:
      self.head = None
      print("List empty after deleting head")
      return
    else:
      self.head = self.head.next
      self.head.prev = None


  def delete_at_end(self):
    if self.head is None:
      print("List is empty")
      return
    if self.head.next is None:
      self.head = None
      print("List empty after deleting head")
      return
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.prev.next = None


  def delete_by_value(self, target):
    if self.head is None:
      print("List is empty")
      return
    if self.head.next is None:
      self.head = None
      print("List empty after deleting")
      return
    if self.head.data == target:
      self.head = self.head.next
      self.head.prev = None
    curr = self.head
    while curr.next is not None:
      if curr.data == target:
         break
      curr = curr.next
    if curr.next is not None:
      curr.next.prev = curr.prev
      curr.prev.next = curr.next
    else:
      if curr.data == target:
        curr.prev.next = None
      else:
        print("Node not found")


  def find_Size(self):
    print()
    curr = self.head
    size = 0
    while curr is not None:
      size += 1
      curr = curr.next
    return size


LL1 = LinkedList()
LL1.insert_at_beginning(10)
LL1.insert_at_beginning(20)
LL1.insert_at_end(30)
LL1.insert_after_node(40, 20)
LL1.insert_before_node(50, 30)
LL1.delete_at_beginning()
LL1.delete_at_end()
LL1.delete_by_value(50)
LL1.printList()
LL1.printList_reverse()
print(LL1.find_Size())