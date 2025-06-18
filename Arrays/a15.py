# add one 

def plusOne(arr):
  n = len(arr)
  for i in range(n-1, -1, -1):
    if arr[i] < 9:
      arr[i] += 1
      return arr
    arr[i] = 0
  return [1] + arr

arr = [1,2,3,4,9]
plusOne(arr)
for i in arr:
  print(i, end=" ")