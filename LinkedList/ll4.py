# check pallindrome

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
        if curr == self.head:
          break


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
    prev = None
    curr = self.head
    while curr is not None:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    return prev
  

  def isIdentical(self,l1,l2):
    while l1 is not None and l2 is not None:
      if l1.data != l2.data:
        return False
      l1 = l1.next
      l2 = l2.next
    return True


  def isPallindrome(self):
    print()
    if self.head is None or self.head.next is None:
      return True
    slow = fast = self.head
    while fast.next is not None and fast.next.next is not None:    #find middle node
      slow = slow.next
      fast = fast.next.next 
    head2 = self.reverse(slow.next)
    slow.next = None
    result = self.isIdentical(self.head, head2)
    slow = self.reverse(head2)
    slow.next = head2
    return result
  

LL1 = LinkedList()
LL1.insert(10)
LL1.insert(40)
LL1.insert(60)
LL1.insert(40)
LL1.insert(10)
LL1.printList()
print(LL1.isPallindrome())