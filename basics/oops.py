# class Student:
#   college_name = "Kiit"   #class attribute

#   def _init_(self):    #default constructor
#     pass

#   def __init__(self, name, marks):   #parameterized constructor
#     self.name = name      #obj attribute(higher priority)
#     self.marks = marks
#     print("hii")

#   def welcome(self):
#     print("welcome student", self.name)

# s1 = Student("hanshika", 87)
# print(s1.name, s1.marks)
# print(s1.college_name)
# s1.welcome()




# class Student:
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   def avg(self):
#     sum = 0
#     for val in self.marks:
#       sum += val
#     print("Avg of",self.name, ":" ,sum/3)

# s1 = Student("hanshika", [97,93,92])
# s1.avg()

# s1.name = "john"
# s1.avg()




# class Student:
#   @staticmethod
#   def college():
#     print("Kiit")
# s1 = Student()
# s1.college()

#abstraction - hiding implementation details and only showing essential data
#encapsulation - wrapping up of data and functions into a single unit(object)

# class BankAccount:
#   def __init__(self, accountNo, balance):
#     self.accountNo = accountNo
#     self.balance = balance

#   def debit(self, amount):
#     self.balance -= amount
#     print(amount, "was debited from", self.accountNo)

#   def credit(self, amount):
#     self.balance += amount
#     print(amount, "was credited to", self.accountNo)

# b1 = BankAccount("abc", 100000)
# b1.credit(500)
# b1.debit(2500)
# print(b1.balance)




# class Student:
#   def _init(self, name):
#     self.name = name
# s1 = Student("hanshika")
# del s1
# print(s1.name)


# class Account:
#   def __init__(self, accNo, accPass):
#     self.accNo = accNo
#     self.__accPass = accPass        #private(__)

#   def reset(self):
#     print(self.__accPass)

# b1 = Account(1234, "abcd")
# print(b1.reset())



# class Car:
#   def __init__(self, type):
#     self.type = type

#   @staticmethod
#   def start():
#     print("car started...")

#   @staticmethod
#   def stop():
#     print("car has stopped...")

# class Toyota(Car):
#   def __init__(self, name, type):
#     self.name = name
#     super().__init__(type)
  
# c1 = Toyota("fortuner", "electric")
# print(c1.name, c1.type)
# c1.start()




# class Person:
#   name = "anonymous"
#   def __init__(self, name):
#     self.name = name
# p1 = Person("rahul")
# print(p1.name)
# print(Person.name)

#p1 and Person generate different names, it can be resolved by

# class Person:
#   name = "anonymous"
#   def __init__(self, name):
#     Person.name = name       #change to self to class name
# p1 = Person("rahul")
# print(p1.name)
# print(Person.name)

#  OR  #

# class Person:
#   name = "anonymous"
#   def __init__(self, name):
#     self.__class__.name = "rahul"       #use this
# p1 = Person("rahul")
# print(p1.name)
# print(Person.name)

#  OR  #

# class Person:
#   name = "anonymous"
#   @classmethod                         #use class method
#   def __init__(cls, name):
#     cls.name = name 
# p1 = Person("rahul")
# print(p1.name)
# print(Person.name)



# class Student:
#   def __init__(self, phy, chem, maths):
#     self.phy = phy
#     self.chem = chem
#     self.maths = maths
  
#   @property
#   def average(self):
#     return str((self.phy + self.chem + self.maths) / 3) + "%"
  
# s1 = Student(83, 96, 91)
# print(s1.average)
# s1.phy = 86
# print(s1.average)



class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img

  def showNumber(self):
    print(self.real, "i +", self.img, "j")

  def __add__(self, num2):
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal, newImg)
  
  def __sub__(self, num2):
    newReal = self.real - num2.real
    newImg = self.img - num2.img
    return Complex(newReal, newImg)
  
num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(3,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()