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
          if curr.next is None:
            print(curr.data, end=" ")
          else:
            print(curr.data, "-->", end=" ")
          curr = curr.next


  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
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


  def insert_after_node(self, data, target):
    curr = self.head
    while curr.next is not None:
      if(curr.data == target):
        break
      else:
        curr = curr.next
    if curr is None:
      print("Node not found")
    else:
      new_node = Node(data)
      new_node.next = curr.next
      curr.next = new_node


  def insert_before_node(self, data, target):
    if self.head is None:
      print("List is empty")
      return
    if self.head == target:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
      return
    curr = self.head
    while curr.next is not None:
      if curr.next.data == target:           #diff part from after node insert
        break
      curr = curr.next
    if curr.next is None:
      print("Node not found")
    else:
      new_node = Node(data)
      new_node.next = curr.next
      curr.next = new_node  


  def delete_at_begining(self):
    if self.head is None:
      print("List is empty")
    else:
      self.head = self.head.next


  def delete_at_end(self):
    if self.head is None:
      print("List is empty")
    elif self.head.next is None:
      self.head = None
    else:
      curr = self.head
      while curr.next.next is not None:
        curr = curr.next
      curr.next = None


  def delete_by_value(self, target):
    if self.head is None:
      print("List is empty")
      return
    elif self.head.data == target:
      self.head = self.head.next
    else:
      curr = self.head
      while curr.next is not None:
        if curr.next.data == target :
          break
        curr = curr.next
      if curr.next is None:
        print("Value not found")
        return
      else:
        curr.next = curr.next.next


  def reverse(self):
    print()
    prev = None
    curr = self.head
    while curr is not None:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    self.head = prev


  def get_nth_node(self, index):
    print()
    curr = self.head
    count = 1
    if self.head is None:
      print("List is empty")
    while curr is not None:
      if count == index:
        return curr.data
      count += 1
      curr = curr.next
    return -1
  

  def nth_node_from_end(self, n):
    slow = fast = self.head
    for _ in range(n):
      if fast is None:
        return -1
      fast = fast.next
    while fast is not None:
      fast = fast.next
      slow = slow.next
    return slow.data


LL1 = LinkedList()
LL1.insert_at_beginning(10)
LL1.insert_at_beginning(20)
LL1.insert_at_end(30)
LL1.insert_after_node(45, 20)
LL1.insert_before_node(67, 10)
LL1.delete_at_begining()
LL1.delete_at_end()
LL1.delete_by_value(67)
LL1.printList()
LL1.reverse()
LL1.printList()
print(LL1.get_nth_node(2))
print(LL1.nth_node_from_end(2))