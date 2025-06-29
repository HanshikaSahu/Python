# check rotation

def isRotation(s1,s2):
  s1 = s1 + s1
  return s2 in s1

s1 = "abc"
s2 = "cab"
print(isRotation(s1, s2))