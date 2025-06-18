# find 2nd largest element

def secondLargest(arr):
  n = len(arr)
  largest = -1
  secondLargest = -1 
  for i in range(n):
    if arr[i] > largest:
      secondLargest = largest
      largest = arr[i]
    elif arr[i] < largest and arr[i] > secondLargest:
      secondLargest = arr[i]
  return secondLargest

arr = [12, 31, 93, 79, 30]
print(secondLargest(arr))