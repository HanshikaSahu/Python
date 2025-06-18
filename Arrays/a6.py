# majority element for floor (N/3) number of elements. arrange in sorted order

def majorityElement(arr):
  n = len(arr)
  candidate1 = -1
  candidate2 = -1
  count1 = 0
  count2 = 0
  for num in arr:
    if count1 == 0:
      candidate1 = num
      count1 = 1
    elif count2 == 0:
      candidate2 = num
      count2 = 1
    elif num == candidate1:
      count1 += 1
    elif num == candidate2:
      count2 += 1
    else:
      count1 -= 1
      count2 -= 1
  
  count = 0
  res = []
  for num in arr:
    if num == candidate1:
      count1 += 1
    if num == candidate2 and candidate1 != candidate2:
      count2 += 1
  
  if count1 > n / 3:
    res.append(candidate1)
  if count2 > n / 3 and candidate1 != candidate2:
    res.append(candidate2)

  if len(res) == 2 and res[0] > res[1]:
    res[0], res[1] = res[1], res[0]

  return res

arr = [1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 1]
res = majorityElement(arr)
for element in res:
  print(element, end=" ")