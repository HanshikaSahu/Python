# 3rd largest element

def third(arr):
  n = len(arr)
  first, second, third = float("-inf"), float("-inf"), float("-inf")
  for i in range(n):
    if arr[i] > first:
      third = second
      second = first
      first = arr[i]
    if arr[i] > second and arr[i] < first:
      third = second
      second = arr[i]
    if arr[i] > third and arr[i] < first and arr[i] < second:
      third = arr[i]
  return third

arr = [12, 31, 93, 79, 30]
print(third(arr))