# remove duplicates

def duplicates(arr):
  n = len(arr)
  if n<1:
    return n
  index = 1   #2nd element
  for i in range(1,n):
    if arr[i] != arr[i-1]:
      arr[index] = arr[i]
      index += 1
  return index

arr = [3,7,1,9,2,2,3]
newSize = duplicates(arr)
for i in range(newSize):
  print(arr[i], end=" ")