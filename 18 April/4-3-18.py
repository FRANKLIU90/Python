# def sum13(nums):
#     if not nums:
#         return 0
#     result = []
#     for x in nums:

#         if x == 13:
#             next(nums)
#             x = 0
#         result.append(x)

#     return sum(result)
# print(list(s))
# from collections import deque


# def missing_char(str, n):
#     str = deque(str)
#     str.pop()
#     return str


# print(missing_char(s, 3))
# print(str[0:3])from itertools import repeat
# from itertools import repeat


# def front3(str):
#     str = str[:3]
#     return repeat(str, 3)


# print(list(front3('Java')))
# print(front3('Chocolate'))
# print(front3('abc'))
# a = ['Jav', 'Jav', 'Jav']
# print(''.join(a))

# def count_evens(nums):
#     return len[x for x in nums if not x % 2]


# print(count_evens([2, 1, 2, 3, 4]))
nums = [13, 1, 13, 13,2, 13, 2, 1, 13]


def max_end3(nums):
  w = max([nums[0] + nums[-1])
  return [w for x in nums]
print(max_end3(nums))

# a = [x for x in nums if not x % 2]
# print(len(a))
# nums += [0]
# result = [x for x in nums if x != 13 and nums[nums.index(x) - 1] != 13]
# print(result)
# print(nums.endswith(13))
# x = [n for i, n in enumerate(nums) if n != 13 and nums[i - 1] != 13]
# print(x)

# this is nort right


# def exclude13(iterable):
#     it = iter(iterable)
#     for x in it:
#         if x == 13:  # don't yield 13
#             next(it)
#             # skip number immediately after 13
#         else:
#             yield x


# # print(list(exclude13(nums)))  # -> 6
# # print(sum(exclude13([1, 2, 13, 2, 1, 13]))) # -> 4
# z = ((1, 0), (0, 1), (1, 1), (0, 0))
# print([(a, b)for a, b in z if a and b])


# def combo_string(a, b):
#     m = [a, b]
#     m = sorted(m, key=len)
#     return '{0}{1}{0}'.format(*m)


# print(combo_string('Hello', 'hi'))
# print(combo_string('aaa', 'b'))
# print(combo_string('', 'Hello'))


# # def count_evens(nums):
# #     return len[x for x in nums if not x % 2]

# indexs = [index for index, x in enumerate(nums) if x == 2]
# for index, num in enumerate(indexs):
#     if indexs[index + 1] = num:
#         return True
