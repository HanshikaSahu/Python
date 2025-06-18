# add until it's a single digit ##

def add(n):
  if n == 0:
    return 0
  elif n % 9 == 0:
    return 9
  else:
    return n % 9
  
print(add(2342))