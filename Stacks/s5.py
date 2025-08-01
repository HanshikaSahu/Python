# 2 stacks in an array

class TwoStacks:
  def __init__(self, size):
    self.size = size
    self.arr =[None] * size
    self.top1 = -1
    self.top2 = size

  def push1(self, x):
    if self.top1 + 1 == self.top2:
      print("Stack overflow")
    else:
      self.top1 += 1
      self.arr[self.top1] = x
      print(f"Pushed {x} to Stack")

  def push2(self, x):
    if self.top2 - 1 == self.top1:
      print("Stack overflow")
    else:
      self.top2 -= 1
      self.arr[self.top2] = x
      print(f"Pushed {x} to Stack")

  def pop1(self):
    if self.top1 == -1:
      print("Stack underflow")
      return None
    else:
      x = self.arr[self.top1]
      self.top1 -= -1
      return x
    
  def pop2(self):
    if self.top2 == self.size:
      print("Stack underflow")
      return None
    else:
      x = self.arr[self.top2]
      self.top2 += -1
      return x
    
s = TwoStacks(10)
s.push1(5)
s.push1(10)
s.push2(15)
s.push2(20)

print("Popped from stack1:", s.pop1())
print("Popped from stack2:", s.pop2())