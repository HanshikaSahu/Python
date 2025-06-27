# reverse words

def reversed(s):
  words = s.split(".")
  reversed_word = words[::-1]
  return ".".join(reversed_word)

s = "..i.like.home.."
print(reversed(s))