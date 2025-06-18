# max product subarray

def maxProduct(arr):
  if arr is None:
    return 0
  max_product = arr[0]
  curr_max = arr[0]
  curr_min = arr[0]

  for i in range(1, len(arr)):
    if arr[i] < 0:  # swap if negative
      curr_max, curr_min = curr_min, curr_max

    curr_max = max(arr[i], arr[i] * curr_max)
    curr_min = min(arr[i], arr[i] * curr_min)

    max_product = max(max_product, curr_max)
  return max_product
  
arr = [1,2,3,4]
print(maxProduct(arr))