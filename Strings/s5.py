#reformat string

def reformat(s, k):
  res = []
  count = 0
  for ch in reversed(s):
    if ch == "-":
      continue
    if count == k:
      res.append("-")
      count = 0
    res.append(ch.upper())
    count += 1
  return " ".join(reversed(res))

s = "5F3Z-2e-9-w"
print(reformat(s, 4))