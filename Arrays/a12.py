# max subarray sum

def maxSubarraySum(arr):
  max_sum = arr[0]
  current_sum = 0
  for num in arr:
    current_sum += num
    if current_sum < 0:
      current_sum = 0
    max_sum = max(current_sum, max_sum)

  return max_sum

arr = [1, 4, 7, 5]
print(maxSubarraySum(arr))