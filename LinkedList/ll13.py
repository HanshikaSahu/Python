# swap kth node from beginning and kth node from end

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


  def count(self):
    count = 0
    curr =self.head
    while curr is not None:
      count += 1
      curr = curr.next
    return count
  

  def swapKth(self, k):
    n = self.count()
    if k > n:
      return
    if 2 * k - 1 == n:   #same node
      return
    prevX = None
    currX = self.head
    for _ in range(k - 1):
      prevX = currX
      currX = currX.next
    prevY = None
    currY = self.head
    for _ in range(n - k):
      prevY = currY
      currY = currY.next
    if prevX is not None:
      prevX.next = currY
    else:
      self.head = currY
    if prevY is not None:
      prevY.next = currX
    else:
      self.head = currX
    currX.next, currY.next = currY.next, currX.next


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(30)  
LL1.insert(40)  
LL1.insert(50)
LL1.swapKth(2)  
LL1.printList()