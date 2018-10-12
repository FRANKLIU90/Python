import os
from functools import partial
os.chdir('/Users/frankyoung/Downloads')
with open('vie-magazine-neil-young-feature.jpg', 'rb') as f:
    with open('copy_neil.jpg', 'wb') as copy_f:
        content = iter(partial(f.read, 1028), '')
        for x in content:
            print(x)
