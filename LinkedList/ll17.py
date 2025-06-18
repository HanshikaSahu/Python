# reverse double linked list in group of k nodes  ###

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


  def reverseKGroup(self, k):
    if self.head is None:
      return
    curr = self.head
    newHead = None
    prevGroupTail = None
    while curr is not None:
      groupHead = curr
      prev = None
      count = 0
      while curr is not None and count < k:
        next_node = curr.next
        curr.next = prev
        curr.prev = next_node
        prev = curr
        curr = next_node
        count += 1
      if newHead is None:
        newHead = prev
      if prevGroupTail is not None:
        prevGroupTail.next = prev
        prev.prev = prevGroupTail
      prevGroupTail = groupHead
    self.head = newHead


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(70)
LL1.insert(50)
LL1.insert(40)
LL1.insert(60)
LL1.insert(30)
LL1.reverseKGroup(3)
LL1.printList()