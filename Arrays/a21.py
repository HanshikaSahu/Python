# remove occurences

def removeOccurences(arr, element):
  k = 0
  for i in range(len(arr)):
    if arr[i] != element:
      arr[k] = arr[i]
      k += 1
  return k

arr = [3,6,8,2]
print(removeOccurences(arr, 2))