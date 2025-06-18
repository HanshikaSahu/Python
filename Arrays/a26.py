# rearrange by sign

def rearrange(arr):
  n = len(arr)
  result = [0] * n
  posIndx = 0
  negIndx = 1
  for num in arr:
    if num >= 0:
       if posIndx < n:
          result[posIndx] = num
          posIndx += 2
    else:
       if negIndx < n:
          result[negIndx] = num
          negIndx += 2
  return result

arr = [2,5,-3,-1,9,0]
print(rearrange(arr))