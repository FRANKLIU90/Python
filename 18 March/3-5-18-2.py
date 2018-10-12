import os
import datetime
# print(os.getcwd())
# os.chdir('/Users/frankyoung/Documents')
# print(os.getcwd())
# os.makedirs('new_folder/new_folder')
# os.makedirs('new_folder/new_folder_2')
# os.removedirs('new_folder')
# os.makedirs('new_folder/1/2/4/5')
# os.removedirs('new_folder/1/2/4/5')
# os.makedirs('new_folder/1/4')
# os.makedirs('new_folder/2')
# os.makedirs('new_folder/1/3/5/6')
# os.rmdir('new_folder/1/3/5')
# print(os.listdir())
# mtime = os.stat('2-5-18 copy.py').st_mtime
# mtime = datetime.datetime.fromtimestamp(mtime)
# time = 'the time is {0:%a} aa {0:%H sdsd %a}  dsdsd {0:%A} and {0:%c}'.format(mtime)
# time_2 = '{:the time is %a aa %H sdsd %a  dsdsd %A and %c}'.format(mtime)
# print(time)
# print(time_2)
# print(time == time_2)


# class Employee():
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay

# @property
# def stat(self):


# emp_1 = Employee('frank', 'young', 50000)
# stat = vars(emp_1)
# words = 'first name is {first},last name is {last}'.format(**stat)
# print(words)

# print(os.environ['HOME'])

# print(os.path.dirname('/Users/frankyoung'))
# print(os.environ.get('HOME'))

# print(os.getcwd())
# for file in os.listdir():
#     print(file)
# ctime = os.stat('3-5-18-2.py').st_ctime
# ctime = datetime.datetime.fromtimestamp(ctime)
# words = 'the year is {0:%Y}, is it a {0:%A},the month is {0:%B},it is in the {0:%-j} days of the year'.format(ctime)
# print(words)
# os.makedirs('dudu/dududu')
# os.rmdir('dudu/dududu')
# for dirpath, dirnames, filenames in os.walk('/Users/frankyoung/Documents'):
#     print(f'the dirpath is {dirpath}')
#     print(f'the dirnames is {dirnames}')
#     print(f'the filenames is {filenames}')
# #     print('')
new_path = os.path.join('/Users/frankyoung/Documents', '2-4-18.py')
# os.rename('2-4-18.py', new_path)
# print(os.environ.get('HOME'))
print(os.path.isfile('2-3-18-2.py'))
