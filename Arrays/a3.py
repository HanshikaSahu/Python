# max product of 3

def maxProduct(arr):
  n = len(arr)
  maxA, maxB, maxC = float("-inf"), float("-inf"), float("-inf")
  minA, minB = float("inf"), float("inf")
  for i in range(n):
    if arr[i] > maxA:
      maxC = maxB
      maxB = maxA 
      maxA = arr[i]
    if arr[i] > maxB and arr[i] < maxA:
      maxC = maxB
      maxB = arr[i]
    if arr[i] > maxC and arr[i] < maxA and arr[i] < maxB:
      maxC = arr[i]

    if arr[i] < minA:
      minB = minA
      minA = arr[i]
    if arr[i] < minB and arr[i] > minA:
      minB = arr[i]

  return max(minA * minB * maxA, maxA * maxB * maxC )


arr = [12, 31, 93, 79, 30]
print(maxProduct(arr))