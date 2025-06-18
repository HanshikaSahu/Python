# construct linked list from 2D matrix   ##

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.down = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    down_node = self.head
    while down_node is not None:
      right_node = down_node
      while right_node is not None:
        print(right_node.data, end=" -> ")
        right_node = right_node.next
      print("None")
      down_node = down_node.down


  def construct2D(self, matrix):
    if matrix is None or matrix[0] is None:
      return
    rows = len(matrix)
    cols = len(matrix[0])
    row_heads = [None] * rows
    prev_row_nodes = [None] * cols
    for i in range(rows):
      prev_node = None
      for j in range(cols):
        new_node = Node(matrix[i][j])
        if prev_node is not None:
          prev_node.next = new_node
        else:
          row_heads[i] = new_node    #make a new row
        if prev_row_nodes[j] is not None:
          prev_row_nodes[j].down = new_node
        prev_row_nodes[j] = new_node
        prev_node = new_node
    self.head = row_heads[0]
  

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
LL = LinkedList()
LL.construct2D(matrix)
LL.printList()