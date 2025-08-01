# delete middle element from stack

def delete_middle(stack, current=0, mid=None):
  if mid is None:
    mid = len(stack) // 2

  if not stack:
    return
  
  x = stack.pop()

  if current != mid:
    delete_middle(stack, current + 1, mid)
    stack.append(x)

stack = [1,2,3,4,5]
print("Original stack:", stack)
delete_middle(stack)
print("Stack after deleting middle:", stack)