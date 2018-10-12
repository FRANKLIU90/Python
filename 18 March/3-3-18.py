# import os
# from functools import partial
# os.chdir('/Users/frankyoung/Downloads')
# with open('vie-magazine-neil-young-feature.jpg', 'rb') as f:
#     with open('copy_neil.jpg', 'wb') as copy_f:
#         chunk = f.read(4096)
#         while len(chunk) > 0:
#             copy_f.write(chunk)
#             chunk = f.read(4096)


# filename = '2-3-18-2.py'

# with open(filename, 'r') as f:
#     with open('copy.py', 'w') as wf:
#         contents = iter(partial(f.read, 32), '')
#         for content in contents:
#             wf.write(content)


# l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# # print(l[1:2])
# m = 'https://www.youtube.com/'
# n = reversed(m)
# print(''.join(n))
# print(m[::-1])
# my_l = (num for num in l)
# for x in my_l:
#     print(x)


# with open('2-5-18.py') as f:
#     my_lines = (line.strip() for line in f if not line.strip().startswith('#') and line.strip())
#     for x in my_lines:
#         print(x)
