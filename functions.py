# 1
# def converttograms():
#     x = int(input())
#     print(x * 28.3495231)
#
#
# converttograms()


# 2
# def celcius():
#     F = int(input())
#     print((5 / 9) * (F - 32))
#
#
# celcius()


# 3
# def solve(numheads, numlegs):
#     ccnt = 0
#     rcnt = 0
#
#     rcnt = (numlegs - 2 * numheads) / 2
#     ccnt = numheads - rcnt
#     print(ccnt, rcnt)
#
#
# numheads = 35
# numlegs = 94
# solve(numheads, numlegs)


# 4
# def filter_prime():
#     l = [int(i) for i in input().split()]
#     for i in range(len(l)):
#         flag = True
#
#         if l[i] != 1:
#             for j in range(2, l[i]):
#                 if (l[i]) % j == 0:
#                     flag = False
#                     break
#             if flag:
#                 print(l[i], end=' ')
#
#
# filter_prime()


# 5
# def permutation(s, l, r):
#     if l == r:
#         print(''.join(s))
#     else:
#         for i in range(l, r):
#             s[l], s[i] = s[i], s[l]
#             permutation(s, l + 1, r)
#
#
# s = input()
# permutation(list(s), 0, len(s))


# 6
# s = input().split(' ')
# l = []
#
# for i in s:
#     l.insert(0, i)
#
# print(' '.join(l))


# 7
# def has_33(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             print(True)
#             return True
#     print(False)
#
#
# nums = [int(i) for i in input().split(', ')]
# has_33(nums)


# 8
# def spy_game(nums):
#     original = [0, 0, 7]
#     l = []
#
#     for i in nums:
#         if i == 0:
#             l.append(0)
#         elif i == 7:
#             l.append(7)
#
#     if l == original:
#         print(True)
#     else:
#         print(False)
#
#
# nums = [int(i) for i in input().split(',')]
# spy_game(nums)



# 9
# def volume():
#     r = int(input())
#     print(4 / 3 * 3.14 * r**3)
#
#
# volume()


# 10
# def new_list(nums):
#     l = []
#
#     for i in nums:
#         if i not in l:
#             l.append(i)
#     print(l)
#
#
# nums = [int(i) for i in input().split(',')]
# new_list(nums)


# 11
# def pal(s, copyy):
#     if s == copyy:
#         print(True)
#     else:
#         print(False)
#
# # s = input()
# copyy = s[::-1]
# pal(s, coppy)


# 12
# def hist(nums):
#     for i in nums:
#         print(i * '*')
#
#
# nums = [int(i) for i in input().split(', ')]
# hist(nums)


# 13
# import random
#
# def guess(x):
#     name = input("Hello! What is your name? ")
#     print("Well, KBTU, I am thinking of a number between 1 and 20.")
#     s = int(input("Take a guess. "))
#
#     cnt = 0
#
#     while s != x:
#         if s < x:
#             print("Your guess is too low.")
#             s = int(input("Take a guess. "))
#         elif s > x:
#             print("Your guess is too high.")
#             s = int(input("Take a guess. "))
#         cnt += 1
#
#     print("Good job, " + name + "! You guessed my number in ", end='')
#     print(cnt, end=' ')
#     print("guesses!")
#
#
# x = random.randint(1, 20)
# guess(x)
