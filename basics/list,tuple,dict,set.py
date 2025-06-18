# list = [2, 4, 1, 5, 3]
# list.append(6)
# print(list)
# print(list.sort())
# print(list)
# print(list.sort(reverse=True))
# print(list)
# print(list.reverse())
# print(list)
# list.insert(2, 10)
# print(list)
# list.remove(10)
# print(list)
# list.pop(2)
# print(list)

# tup = (1, 2, 3, 4, 5)
# print(tup, type(tup), len(tup))
# tup([0]) = 10   #tuples are immutable
# print(tup)
# tup = (1)
# print(type(tup))
# tup = ("hello")
# print(type(tup))
# print(tup.index("l"))
# print(tup.count("l"))

#check pallindrome
# list = [1,2,3,2,1]
# listCopy = list.copy()
# listCopy.reverse()
# if(listCopy == list):
#   print("Pallindrome")
# else:
#   print("not a pallindrome")

# dict = {
#   "name": "hanshika",
#   "age": 21,
#   "marks": 94.4
# }
# print(dict, type(dict))    #unordered(no indexes) and mutable
# print(dict["name"])
# dict["name"] = "HanshikaSahu"
# print(dict["name"])

#nested dictionary
# dict = {
#   "name": "Hanshika",
#   "subjects" : {
#     "phy": 93,
#     "chem": 97,
#     "bio": 98
#   },
#   "age": 21
# }
# print(dict["subjects"]["chem"])
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("subjects"))
# new_dict = {
#   "name": "hanshika",
#   "age": 21,
#   "city": "rnc"
# }
# dict.update(new_dict)
# print(dict)

# set = {1,2,2,2}    #unordered and unique(duplicates ignored) 
# print(set)         ##sets are mutable but it's elements are immutable
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add("hello")
# collection.add((1,2,3))
# print(collection)
# collection.remove(1)
# print(collection)      #lists cannot be added as they are mutable
# # collection.clear()
# # print(collection)
# collection.pop()
# print(collection)

# set1 = {1,2,3,4}
# set2 = {4,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))

#store 9 and 9.0 seperately
# set = {9, "9.0"}
# print(set)       ##make a value string
### OR ###
# dict = {
#   "int": 9,
#   "float": 9.0
# }
# print(dict.values())     ##store as dict and get their values