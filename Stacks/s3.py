# queue using stack

class QueueUsingStack:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, value):
    self.stack1.append(value)

  def dequeue(self):
    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())
    if not self.stack2:
      print("Queue is empty")
      return None
    return self.stack2.pop()
  
  def display(self):
    result = self.stack2[::-1] + self.stack1
    print("Queue:", result)
  

q = QueueUsingStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("Dequeued:", q.dequeue())
q.display()