# max consecutive count

def maxCount(arr):
  n = len(arr)
  maxCount, count = 0, 1
  for i in range(1, n):
    if arr[i] == arr[i - 1]:
      count += 1
    else:
      maxCount = max(maxCount, count)
      count = 1
  return max(maxCount, count)

arr = [1, 2, 1, 1 , 1, 5]
print(maxCount(arr))