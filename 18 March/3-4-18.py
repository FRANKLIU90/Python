import datetime

# today = datetime.datetime.today()
# print(today)

# my_words = 'today is {0:%c}, it is in {0:%B},it is the {0:%j} of the year,{0:%A}'.format(today)
# print(my_words)
names = ['john', 'abear', 'frank', 'young']

# my_words = f'my name is {names[0]}, his name is {names[2]}'
my_words='my name is {0}, his name is {2}'.format(*names)
print(my_words)
