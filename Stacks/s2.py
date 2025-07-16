# postfix to prefix

def postToPre(postfix):
  stack = []
  operators = set("+-*/^%")
  for c in postfix:
    if c not in operators:
      stack.append(c)
    else:
      a = stack.pop()
      b = stack.pop()
      stack.append(c + b + a)
  return stack[0]

postfix = "AB+CD-*"
print(postToPre(postfix))