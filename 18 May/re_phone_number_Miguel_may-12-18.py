
numbers = """5121234567
512 123 4567
512 123-4567
(512)1234567
(512) 1234567
(512) 123-4567
(512) 123 4567
512--123-4567
512  123  4567
512 l23 4567  (expect error)
(512) 12E 4567  (expect error)
512.123.4567
(512) 123 456  (expect error)
(512 123 4567
512) 123 4567"""

import re
pattern = re.compile(r'\(?(\d{3})\)?.{0,2}(\d{3}).{0,2}(\d{4})')
for num in numbers.split('\n'):
    match = pattern.findall(num)

    if match:
        sub = pattern.sub(r'(\1)-\2 \3', num)
        print(f'found it! {num}---->{sub}')
    if not match:
        print(f'error! {num}')

   # if not sub:
    #     print('nono')
    #     print(f'error! {num}')
    # match = pattern.findall(num)

    # if not match:
    #     print(f'error! {num}')
    # else:
    #     print(f'found it! {match[0]}')


# 12 good 3 bad
# print(len(numbers.split('\n')))

"""5121234567 #
# 512 123 4567
# 512 123-4567
# (512)1234567
# (512) 1234567
# (512) 123-4567
# (512) 123 4567
# 512--123-4567
# 512  123  4567
# 512 l23 4567  (expect error)
# (512) 12E 4567  (expect error)
# 512.123.4567
# (512) 123 456  (expect error)
 # (512 123 4567
# 512) 123 4567"""
# print(list(st.split('\n')))
# good = ['5121234567', '512 123 4567', '512 123-4567', '(512)1234567', '(512) 1234567', '(512) 123-4567', '(512) 123 4567', '512--123-4567', '512  123  4567', '512.123.4567', ' (512 123 4567', '512) 123 4567']
# bad = ['(512) 123 456  (expect error)', '512 l23 4567  (expect error)', '(512) 12E 4567  (expect error)', ]
# good = ' ***** '.join(good)
# print(good)

# pattern = re.compile(r'\(?\d{3}\)?.?.?\d{3}.?.?\d{4}')
# matches = pattern.finditer(numbers)
# print(len(list(matches)))
# for match in matches:
#     print(match)

# back up
# pattern = re.compile(r'\(?\d{3}\)?.{0,2}\d{3}.{0,2}\d{4}')
# for num in numbers.split('\n'):

#     match = pattern.findall(num)

#     if not match:
#         print(f'error! {num}')
#     else:
#         print(f'found it! {match[0]}')
