# reverse in k groups

def reverseKGroups(arr, k):
  i = 0
  n = len(arr)
  while i < n:
    left = i
    right = min(i + k - 1, n - 1)
    while left < right:
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1
    i += k

arr = [1, 2, 3, 4, 5, 6]
reverseKGroups(arr, 3)
for el in arr:
  print(el, end=" ")