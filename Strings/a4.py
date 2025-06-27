# string to integer   (atoi method)

def convert(s:str) -> int:
  sign = 1
  i = 0
  res = 0

  #ignore blank spaces
  while i < len(s) and s[i] == " ":
    i += 1

  #sign
  if i < len(s) and (s[i] == "-" or s[i] == "+"):
    if s[i] == "-":
      sign = -1
    i += 1

  while i < len(s) and "0" <= s[i] <= "9":
    res = 10 * res + (ord(s[i]) - ord("0"))   #ord-> stores ascii values   ord("0")=48, 1->49, 2->50    
                                              #ord(s[i])-ord("0") = 50 - 48 = 2(integer) 

    if res > (2**31 - 1):
      return sign * (2**31 - 1) if sign == 1 else -2**31
    
    i += 1
    
  return res * sign

s = "-0012afg4"
print(convert(s))