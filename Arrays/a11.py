# find min height  ## 

def minHeight(arr, k):
  arr.sort()
  n = len(arr)
  answer = arr[n-1] - arr[0]

  smallest = arr[0] + k
  largest = arr[n - 1] - k

  for i in range(n - 1):
    min_element = min(smallest, arr[i + 1] - k)
    max_element = max(largest, arr[i] + k)

    if min_element < 0:
      continue

    answer = min(answer, max_element - min_element)
  return answer

arr = [1, 3, 6, 9, 5]
print(minHeight(arr, 2))