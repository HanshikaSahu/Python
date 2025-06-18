# leader in array   (leader -> highest value)

def leader(arr):
  result = []
  n = len(arr)
  maxRight = arr[-1]    # start from last element
  result.append(maxRight)
  for i in range(n-2, -1, -1):
    if arr[i] >= maxRight:
      maxRight = arr[i]
      result.append(maxRight)
  result.reverse()
  return result

arr = [2,4,16,7,8]
print(leader(arr))