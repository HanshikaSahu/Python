# find pairs for a given sum in sorted double linked list

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


  def find_pairs(self, target):
    result = []
    slow = fast = self.head
    while fast.next is not None:   
      fast = fast.next           #bring fast to end node
    while slow != fast and fast.next != slow:
      if (slow.data + fast.data) == target:
        result.append((slow.data, fast.data))
        slow = slow.next
        fast = fast.prev
      elif (slow.data + fast.data) < target:
        slow = slow.next
      else:
        fast = fast.prev
    return result

LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(30)
LL1.insert(40)
LL1.insert(50)
target = 70
pairs = LL1.find_pairs(target)
if not pairs:
  print("No pairs found")
else:
  for pair in pairs:
    print(pair[0], pair[1])