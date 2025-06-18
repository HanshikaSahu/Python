# merge 2 sorted linked list

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

  
  def mergeSort(self, head1, head2):
    if head1 is None:
      return head2
    if head2 is None:
      return head1
    if head1.data <= head2.data:
      head1.next = self.mergeSort(head1.next, head2)
      return head1
    else:
      head2.next = self.mergeSort(head2.next, head1)
      return head2
    
LL1 = LinkedList()
LL1.insert(10)
LL1.insert(40)
LL1.insert(60)
LL1.printList()
LL2 = LinkedList()
LL2.insert(20)
LL2.insert(30)
LL2.insert(50)
LL2.printList()
merged = LL1.mergeSort(LL1.head,LL2.head)
print("Merged list: ")
curr = merged
while curr is not None:
  print(curr.data, end=" ")
  curr = curr.next