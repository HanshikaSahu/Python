# def sum(a,b):
#   s = a + b
#   return s
# print(sum(3,4))

#print elements of list in a single line
# heros = ["ironman", "captain america", "thor", "loki", "doomsday"]
# def printList(list):
#    for hero in heros:
#       print(hero, end=" ")
# printList(heros)

# def show(n):
#   if(n == 0):     #if(n==0) is base statement of recursion
#     return
#   print(n)
#   show(n-1)
# show(5)

# def fact(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#     return n * fact(n-1)
# print(fact(4))

# f = open("demo.txt", "r")
# data = f.read()
# print(data, type(data))
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

# f = open("demo.txt", "w")
# f.write("Hello")
# f.close()
# f = open("demo.txt", "a")
# f.write("How u doin")
# f.close()
# with open("demo.txt") as f:
#   data = f.read()
#   print(data)

# import os
# os.remove("demo2.txt")

# with open("demo2.txt", "w") as f:
#   f.write("Hi everyone\nWe are learning file io\n")
#   f.write("using Java.\nI love learning Java")
  
# with open("demo2.txt", "r") as f:
#   data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)
# with open("demo2.txt", "w") as f:
#   f.write(new_data)

# def word_in_txt():
#   word = "learning"  
#   with open("demo2.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#       print("Found")
#     else:
#       print("NOT found")
# word_in_txt()

# def word_in_line():
#   word = "learning"
#   line = 1
#   data = True
#   with open("demo2.txt", "r") as f:
#     while data:
#       data = f.readline()
#       if(word in data):
#         print(line)
#         return
#       line += 1
#   return -1
# word_in_line()