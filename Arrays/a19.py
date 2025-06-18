# buy and sell in one transaction to find max profit (1 buy + 1 sell)

def maxProfit(arr):
  minSoFar = arr[0]
  res = 0
  for i in range(1, len(arr)):
    minSoFar = min(minSoFar, arr[i])
    res = max(res, arr[i] - minSoFar)
  return res

prices = [3,6,8,1]
print(maxProfit(prices))