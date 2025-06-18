# find 0 with farthest 1s in binary array

import math

def findDistance(arr):
  res = -1
  emptyCount = 0
  for i in range(len(arr)):
    if arr[i] == 0:
      emptyCount += 1
    elif arr[i] == 1:
      res = emptyCount
      emptyCount = 0
    else:
      res = max(res, math.ceil(emptyCount / 2))       # ceil -> round off to nearest integer(1.5->2)
      emptyCount = 0
  res = max(res, emptyCount)
  return res

arr = [1,0,1,0,0,0,1]
print(findDistance(arr))