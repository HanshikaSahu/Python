# zeros to end

def zerosToEnd(arr):
  count = 0
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[i], arr[count] = arr[count], arr[i]
      count += 1

arr = [1, 2, 0, 5, 0, 3]
zerosToEnd(arr)
for element in arr:
  print(element, end=" ") 