# find max profit

def maxProfits(prices):
  result = 0
  for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
      result += prices[i] - prices[i-1]
  return result

prices = [12, 45, 2222, 89, 65]
print(maxProfits(prices)) 