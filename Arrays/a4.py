# next permutation ###

def next_permutation(arr):
  i = len(arr) - 2
  #find the first decreasing element from the end
  while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1
  #if found one, swap it with the next greater element
  if i >= 0:
    j = len(arr) - 1
    while arr[j] <= arr[i]:
      j -= 1
    arr[i], arr[j] = arr[j], arr[i]
  #reverse the elements after i
  arr[i + 1:] = reversed(arr[i + 1:])

arr = [1, 2, 3, 4]
next_permutation(arr)
print(arr)