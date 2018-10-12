# Customer_Satisfaction.csv
import csv


# class Iter_info:
#     def __init__(self, path, mode='r'):
#         self.path = path
#         self.mode = mode

#     def __iter__(self):
#         with open(self.path) as f:
#             reader = csv.DictReader(f)
#             for line in reader:
#                 yield line


# # print(iter(Iter_info('Customer_Satisfaction.csv')) is iter(Iter_info('Customer_Satisfaction.csv')))
# # print(next(iter(Iter_info('Customer_Satisfaction.csv'))))
# # print(next(iter(Iter_info('Customer_Satisfaction.csv'))))
# for info in Iter_info('Customer_Satisfaction.csv'):
#     print(info['Year'])
# print('zzz')
# for info in Iter_info('Customer_Satisfaction.csv'):
#     print(info['Year'])
# with open('Customer_Satisfaction.csv') as f:
#     reader = csv.DictReader(f)
#     with open('Customer_Satisfaction_copy.csv', 'w')as wf:
#         fieldnames = ['Year',  'Category']
#         writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter='\t')
#         writer.writeheader()
#         for line in reader:
#             del line['Satisfaction Rating']
#             writer.writerow(line)
# with open('Customer_Satisfaction.csv') as f:
#     reader = csv.DictReader(f)
#     with open('Customer_Satisfaction_copy.csv', 'w') as wf:
#         fieldnames = ['Year', 'Category']
#         writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter='\t')
#         writer.writeheader()
#         for line in reader:
#             del line['Satisfaction Rating']
#             writer.writerow(line)
# from functools import wraps


# def cache_with_prefixdict(saved=None):
#     if saved is None:
#         saved = {}

#     def cache(my_func):
#         @wraps(my_func)
#         def wrapper(*args):
#             print(saved)
#             if args in saved:
#                 print('return from saved')
#                 return saved[args]

#             result = my_func(*args)
#             saved[args] = result
#             print('new get')
#             return result
#         return wrapper
#     return cache


# @cache_with_prefixdict(saved={(1,): 12})
# def func(x):
#     return x**2


# print(func(1))
# # print(func(1))
# s = 'return from saved'
# nums = [183, 32, 4, 1, 2, 4, 3, 5]
# nums[2:5] = []
# print(nums)
clas
