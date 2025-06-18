# number of subarrays having prduct less than k

def countSubarraysWithProductLessThanK(arr, k):
  if k<= 1:
    return 0
  count = 0
  left = 0
  product = 1
  for right in range(len(arr)):
    product *= arr[right]
    while product >= k:
      product //= arr[left]
      left += 1

    count += right - left + 1
  return count

arr = [2, 5, 7]
print(countSubarraysWithProductLessThanK(arr, 30))