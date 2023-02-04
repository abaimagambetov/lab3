# 1
# class stringmethods:
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input()
#     def printString(self):
#         print(self.s.upper())
#
#
# s = stringmethods()
# s.getString()
# s.printString()


# 2
# class Shape:
#     def __init__(self):
#         self.a = 0
#     def area(self):
#         return 0
#
# class Square(Shape):
#     def __init__(self, a):
#         super().__init__()
#         self.length = a
#     def area(self):
#         print(self.length ** 2)
#
#
# x = int(input())
# s = Square(x)
# s.area()


# 3
# class Shape:
#     def __init__(self):
#         self.l = None
#         self.w = None
#
#     def area(self):
#         return 0
#
#
# class Rectangle(Shape):
#     def __init__(self, l, w):
#         super().__init__()
#         self.l = l
#         self.w = w
#
#     def area(self):
#         print(l * w)
#
#
# l = int(input())
# w = int(input())
# ans = Rectangle(l, w)
# ans.area()


# 4
# import math
# class Point:
#     def __init__(self):
#         self.a = 0
#         self.b = 0
#         self.c = 0
#         self.d = 0
#
#     def getpoint(self):
#         self.a = int(input())
#         self.b = int(input())
#
#     def display(self):
#         print(self.a, self.b)
#
#     def move(self):
#         self.c = int(input("coordinate 'c': "))
#         self.d = int(input("coordinate 'd': "))
#
#     def distance(self):
#         print(math.sqrt((self.a - self.c) ** 2 + (self.b - self.d) ** 2))
#
#
# s = Point()
# s.getpoint()
# s.display()
# s.move()
# s.distance()


# 5
# class Account:
#     def __init__(self):
#         self.owner = ""
#         self.balance = 1000 # for example
#
#     def name_owner(self):
#         self.owner = input("Name: ")
#
#     def show_balance(self):
#         print("Your balance is:", self.balance)
#
#     def deposit(self):
#         x = int(input("Enter your deposit money: "))
#         self.balance += x
#         print("Success!")
#
#     def withdrawal(self):
#         x = int(input("Enter your withdrawal money: "))
#
#         if x > self.balance:
#             print("Fail! Your balance is lower than the withdrawal money. Try again.")
#         else:
#             self.balance -= x
#             print("Success!")
#
#
# s = Account()
# s.name_owner()
# s.show_balance()
# s.deposit()
# s.show_balance()
# s.withdrawal()
# s.show_balance()


# 6
def filter(l):
    for i in l:
        if i < 2:
            continue

        else:
            flag = 0
            for j in range(2, i - 1):
                x = lambda: i % j == 0
                if x():
                    flag = 1
                    break
            if flag == 0:
                print(i, end=' ')


l = [int(i) for i in input().split()]
filter(l)