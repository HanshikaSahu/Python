# stack using queue

from queue import Queue

class StackUsingQueue:
  def __init__(self):
    self.queue1  = Queue()
    self.queue2  = Queue()
  
  def push(self, x):
    self.queue1.put(x)
    print("Pushed:", x)

  def pop(self):
    if self.queue1.empty():
      print("Stack is empty")
      return None
    while self.queue1.qsize() > 1:
      self.queue2.put(self.queue1.get())

    popped = self.queue1.get()
    print("Popped: ", popped)

    self.queue1, self.queue2 = self.queue2, self.queue1
    return popped
  
  def top(self):
    if self.queue1.empty():
      print("Stack is empty")
      return None

    while self.queue1.qsize() > 1:
      self.queue2.put(self.queue1.get())

    top = self.queue1.get()
    self.queue2.put(top)

    self.queue1, self.queue2 = self.queue2, self.queue1
    print("Top: ", top)
    return top
  
  def empty(self):
    return self.queue1.empty()
  
  
s = StackUsingQueue()
s.push(1)
s.push(2)
s.push(3)
s.top()
s.pop()
s.top()