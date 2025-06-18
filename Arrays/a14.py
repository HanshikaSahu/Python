# sort in wave form

def sortInWaveForm(arr):
  n = len(arr)
  for i in range(0, n, 2):
    if i>0 and arr[i] < arr[i-1]:
      arr[i], arr[i-1] = arr[i-1], arr[i]
    if i<n-1 and arr[i] < arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
    
arr = [1, 3, 5, 6, 4, 8, 2]
sortInWaveForm(arr)
for i in arr:
  print(i, end=" ")