# rotate array by k elements

def rotateArray(arr, k):
  n = len(arr)
  k = k % n # when k is grater than n
  reverse(arr, 0 , k-1)
  reverse(arr, k , n-1)
  reverse(arr, 0 , n-1)

def reverse(arr, start, end):
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

arr = [1,2,3,5,1,8,4,9,3,4,5]
rotateArray(arr, 3)
for i in arr:
  print(i, end=" ")