# multiply numbers in linked list

MOD = 1000000007

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  

  def printList(self, head=None):
    if head is None:
      print("Linked list is empty")
    else:
      curr = head
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


  def multiply(self, first, second):
    num1 = 0
    num2 = 0
    while first is not None:
      num1 = (num1 * 10 + first.data) % MOD
      first = first.next
    while second is not None:
      num2 = (num2 * 10 + second.data) % MOD
      second = second.next
    return (num1 * num2) % MOD
  

LL1 = LinkedList()
LL1.insert(1)
LL1.insert(2) 
LL2 = LinkedList()
LL2.insert(3) 
LL2.insert(0) 
print(LL1.multiply(LL1.head, LL2.head))