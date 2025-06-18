#split circular list into 2 circular lists

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
      print("back to head")


  def insert(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      new_node.next = self.head
    else:
      curr = self.head
      while curr.next != self.head:
        curr = curr.next
      curr.next = new_node
      new_node.next = self.head


  def split_list(self):
    slow = self.head
    fast = self.head
    if self.head is None:
      return
    while fast.next != self.head and fast.next.next != self.head:        #odd no.s->fast.next = head
      fast = fast.next.next                                              #even no.s->fast.next.next = head
      slow = slow.next                                                   #since fast moves 2 steps ahead
    if fast.next.next == self.head:
      fast = fast.next             #make fast now move 1 step ahead if even no.s
    head1 = self.head
    head2 = slow.next
    fast.next = head2
    slow.next = head1
    list1 = LinkedList()
    list2 = LinkedList()
    list1.head = head1
    list2.head = head2
    return list1, list2


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(40)
LL1.insert(70)
LL1.insert(90)
LL1.insert(20)
list1,list2 = LL1.split_list()
list1.printList()
list2.printList()