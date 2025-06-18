# adding numbers   ##

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


  def reverse(self, head):
    curr = head
    prev = None
    while curr is not None:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    return prev
  

  def trimZeros(self, head):
    while head is not None and head.data == 0:
      head = head.next
    return head
  

  def countNodes(self, head):
    length = 0
    curr = head
    while curr is not None:
      length += 1
      curr = curr.next
    return length
  

  def addNumbers(self, num1, num2):
    num1 = self.trimZeros(num1)
    num2 = self.trimZeros(num2)
    len1 = self.countNodes(num1)
    len2 = self.countNodes(num2)
    if len1 < len2:
      return self.addNumbers(num2, num1)
    carry = 0
    num1 = self.reverse(num1)
    num2 = self.reverse(num2)
    result = num1
    while num2 is not None or carry != 0:
      num1.data += carry
      if num2 is not None:
        num1.data += num2.data
        num2 = num2.next
      carry = num1.data // 100
      num1.data = num1.data % 100
      if num1.next is None and carry != 0:
        num1.next = Node(0)
      num1 = num1.next
    return self.reverse(result)


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(30)  
LL2 = LinkedList()
LL2.insert(30)
LL2.insert(20)
LL2.insert(10) 
result = LL1.addNumbers(LL1.head,LL2.head)
LL1.printList(result)