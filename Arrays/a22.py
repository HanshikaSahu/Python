# split into three segments such that 
# sum[0...i] == sum[i+1...j] == sum[j...len(arr)]

def splitIntoThree(arr):
  res = []
  total = 0
  for element in arr:
    total += element
  if total % 3 != 0:
    res = [-1, -1]
    return res
  
  currSum = 0
  for i in range(len(arr)):
    currSum += arr[i]
    if currSum == total / 3:
      currSum = 0
      res.append(i)

      if len(res) == 2 and i < len(arr) - 1:
        return res
  res = [-1, -1]
  return res

arr = [2,4,7,3,6,5]
print(splitIntoThree(arr))