# largest word in dict

def isSubsequence(s1,s2):
  m, n = len(s1), len(s2)
  j = 0
  for i in range(n):
    if s1[j] == s2[i]:
      j += 1
    if j == m:
      break
  return j == m
  
def longestWord(dict, str):
  result = ""
  length = 0
  for word in dict:
    if length < len(word) and isSubsequence(word, str):
      result = word
      length = len(word)
  return result

dict = ["pintu", "geeksfor", "geeksgeeks", "forgeek"]
str = "geeksforgeeks"
print(longestWord(dict, str))