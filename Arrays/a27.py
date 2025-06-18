# Insert an adjacent duplicate for all occurrences of a given element  ##

def duplicate_k(arr, k):
  n = len(arr)
  count = arr.count(k)
  write_index = n + count -1
  curr = n - 1
  while curr >= 0 and write_index >= 0:
    if write_index < n:
      arr[write_index] = arr[curr]
    write_index -= 1

    if arr[curr] == k:
      if write_index < n:
        arr[write_index] = k
      write_index -= 1
    curr -= 1
  return arr

arr = [2,1,2,5,7]
print(duplicate_k(arr, 2))