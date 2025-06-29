# longest common prefix

def longestCommonPrefix(arr):
  arr.sort()
  first = arr[0]
  last = arr[-1]
  minLength = min(len(first), len(last))
  i = 0
  while i < minLength and first[i] == last[i]:
    i += 1
  return first[:i]

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(longestCommonPrefix(arr))