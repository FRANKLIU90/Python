
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

pattern = re.compile(r'\(?(\d{3})[.)\s-]{0,2}(\d{3})[. -]{0,2}(\d{4}zz)')

# for number in numbers.split('\n'):

matches = pattern.finditer(numbers)
print(list(matches))
