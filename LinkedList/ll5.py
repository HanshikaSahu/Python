# remove occurences      ##

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

  
  def findKey(self):
    max_count = 0
    most_freq = self.head
    outer = self.head
    while outer is not None:
      count = 0
      inner = self.head
      while inner is not None:
        if outer.data == inner.data:
          count += 1
        inner = inner.next
      if count > max_count:
        max_count = count
        most_freq = outer.data
      outer = outer.next
    return most_freq
  

  def occurences(self, key):
    while self.head is not None and self.head.data == key:
      self.head = self.head.next
    prev = None
    curr = self.head
    while curr is not None:
      if curr.data == key:
        if prev is None:
          self.head = curr.next
        else:
          prev.next = curr.next
        curr = curr.next
      else:
        prev = curr
        curr = curr.next
    return self.head
  

LL1 = LinkedList()
LL1.insert(10)
LL1.insert(10)
LL1.insert(40)
LL1.insert(60)
LL1.insert(60)
LL1.insert(10)
LL1.printList()
key = LL1.findKey()
LL1.occurences(key)           #10 is key and not 60, as it appears more times 
LL1.printList()