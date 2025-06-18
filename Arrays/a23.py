# max consecutive ones after flipping zeros

def maxOnes(arr, k):
  res = 0
  start = 0
  end = 0
  count = 0  # count zeros
  while end < len(arr):
    if arr[end] == 0:
      count += 1

    while count > k:
      if arr[start] == 0:
        count -= 1
      start += 1
    res = max(res, (end - start + 1))
    end += 1
  return res

arr = [1,1,1,0,1,0,1,1,1]
print(maxOnes(arr, 1))