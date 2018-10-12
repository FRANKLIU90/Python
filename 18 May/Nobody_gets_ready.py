# string formatting
from math import pi
import datetime

lst = ['python', 'java']
dct = {'name': 'frank', 'age': 27}
dt = datetime.date.today()
str_formatting = 'the pi is {0:07,.2f}, my name is {name}, i am {age} years old,i am learing {1} and {2} ,today is {3:%B %Y %d}'.format(pi, *lst, dt, **dct)
print(str_formatting)#the pi is 0,003.14, my name is frank, i am 27 years old,i am learing python and java ,today is May 2018 12

# tried {name.upper()} ,Not Supported./AttributeError: 'str' object has no attribute 'upper()'
# "cant not use method call in ''.format(),only subscription (indexing by number or by unquoted (!) name), and attribute access is supported.but f'{name.upper()}' works.
name = 'frank'
print(f'{name.upper()}') #FRANK
try:
    print('{.upper()}'.format(name))
except AttributeError as e:
    print(e) #'str' object has no attribute 'upper()'

# any(iterable) all(iterable)
print(all(()) is True) #so true
print(any(())) #False

lst=['a',1,'b']
try:
    print(''.join(lst))
except Exception as e:
    print(e) #sequence item 1: expected str instance, NoneType found
# join is a str method, only works for string. not int or NoneType

print('a'[:4])#--->No Error ,gets 'a'
print('a'[:-4]) #No Error,''empty str
try:
    print('a'[-4])
except Exception as e:
    print(e) #sequence item 1: expected str instance, int found


import csv
import contextlib
# file doesnt exist,the point is DictReader.DictWriter is much easier to use,and you can modify the the new csv's info order, but you will have to modify the fieldnames first. keyword args has no order.
with contextlib.suppress(Exception):
    with open('Customer_Satisfaction.csv') as rf:
        reader = csv.DictReader(rf)
        print(reader.fieldnames)  # ['Year', 'Category', 'Satisfaction Rating']
        with open('Customer_Satisfaction_copy.csv', 'w') as wf:
            fieldnames = ['Category', 'Year']
            writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            for line in reader:
                del line['Satisfaction Rating']
                writer.writerow(line)


# Sort file into year_month folder
import os
import datetime
from contextlib import suppress
def year_month_folder(path):
    os.chdir(path)
    for file in os.listdir():
        if os.path.isfile(file):

            mtime = os.stat(file).st_mtime
            mtime = datetime.date.fromtimestamp(mtime)
            folder_name = f'{mtime:%y %B}'
            with suppress(FileExistsError):#or you can use os.path.exists() as a condition,but at <Raymond Hettinger's Transforming Code into Beautiful, Idiomatic Python>-43:28 ,he said it is not a good way,because it has a raise condition in it.I don't know why.
                os.mkdir(folder_name)

            name_path = os.path.join(folder_name, file)
            os.rename(file, name_path)



"""object sorting"""
from operator import itemgetter, attrgetter, methodcaller

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(student_tuples, key=itemgetter(2)))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(sorted(student_tuples, key=itemgetter(1, 2)))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [Student('john', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10), ]

print(sorted(student_objects, key=attrgetter('age')))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(sorted(student_objects, key=attrgetter('grade', 'age')))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

messages = ['critical!!!', 'hurry!', 'standby', 'immediate!!']
print(sorted(messages, key=methodcaller('count', '!')))
# ['standby', 'hurry!', 'immediate!!', 'critical!!!']


"""contextmanger"""
import os
import glob
import contextlib


@contextlib.contextmanager
def find_py(path):
    ori_path = os.getcwd()
    try:
        os.chdir(path)
        result = glob.glob('*.py')
        yield result
    finally:
        os.chdir(ori_path)


# with find_py('/Users/frankyoung/Documents/Python3/18 March') as f:
#     for pyfile in f:
#         print(pyfile)
# print(os.getcwd())

# or use a class
class Find_Py:
    def __init__(self, path):
        self.path = path
        self.ori_path = os.getcwd()

    def __enter__(self):
        os.chdir(self.path)
        result = glob.glob('*.py')
        return result

    def __exit__(self, exc_type, exc_val, traceback):
        os.chdir(self.ori_path)


# with Find_Py('/Users/frankyoung/Documents/Python3/18 March') as f:
#     for pyf in f:
#         print(pyf)
# print(os.getcwd())


@contextlib.contextmanager
# by Nick Coghlan
def suppress(*exceptions):
    try:
        yield
    except exceptions:
        pass


# Decorator,Scope,Closure
# the LEGB rule , for accessing(say,print) and modifying(append) mutable var only.But not reasigning after referenced to a nonlocal(enclosing,Global) variable .
# UnboundLocalError: local variable referenced to  before assignment.

"the scope of a var is determined when function is defined , the value of a var is determined when the function is called"
# <Thomas Ballinger - Finding closure with closures - PyCon 2016>"It turns out that Python analyzes function source code, even compiles it, when a function is defined. During this process it determines the scope of each variable. This determines the process that will be used to find the value of each variables, but does not actually look up this value yet."


# https://nedbatchelder.com/text/names.html
# Ned Batchelder - Facts and Myths about Python names and values - PyCon 2015
'so when the function returns, those names go away. But if the values they refer to are still referenced by other names, the values live on.--nedbatchelde'
# 'so when the function returns, those names go away.'i like to see it as when a function return ,the local var is not accessable from the global scope, i don't know if they disappear or not. maybe like ned said, 'if the values they refer to are still referenced by other names, the values live on(for thoese other names)' like what we have seen from a closure.

a = 1
def p():
    print(a)

a = 2
def w():
    print(a)

p()  # 2,because a`s scope is determined as a global var when the function was defined, when the func call , it look up the global a`s value by then, which is 2.
w()  # 2


# http://docs.python-guide.org/en/latest/writing/gotchas/
# Late Binding Closures
funcs = [lambda x: x * i for i in range(3)]  # by the way , i here is a local var.so i doesnt not exist in the global scope.if try to print i , 'NameError: name 'i' is not defined'
for func in funcs:
    print(func(2))
# 4,4,4
# same :you will get 2*2=4,2*2=4,2*2=4,because the three 'i's  are in the same scope,when the functions is called , i=2.so you get 4,4,4.
# Solution #1:use keyword args.'Python’s default arguments are evaluated once when the function is defined, not each time the function is called '
funcs = [lambda x, i=i: x * i for i in range(3)]
for func in funcs:
    print(func(2))
# 0,2,4
# Solution #2 you can use generator expression, without keyword args.because generator look up the value as it goes.
funcs = (lambda x: x * i for i in range(3))
for func in funcs:
    print(func(2))
# 0,2,4
#
# https://www.google.com/search?q=after+the+golden+rush&rlz=1C5CHFA_enUS782US782&oq=after+the+golden+rush&aqs=chrome..69i57j0l5.988j0j1&sourceid=chrome&ie=UTF-8
# python's scope for class
# "As provided in other answers, there are 4 basic scopes, the LEGB, for Local, Enclosing, Global and Builtin. In addition to those, there is a special scope, the class body, which does not comprise an enclosing scope for methods defined within the class; any assignments within the class body make the variable from there on be bound in the class body."
x = 0
class X(object):
    y = x
    x = x + 1 # x is now a variable
    z = x

    def method(self):
        print(self.x) # -> 1
        print(x)      # -> 0, the global x
        print(y)      # -> NameError: global name 'y' is not defined

inst = X()
print(inst.x, inst.y, inst.z, x) # -> (1, 0, 1, 0)

'function attribute, functions can have attributes.'
# in python , functions can have attribute.

# make a counter decorator using function attr.
from functools import wraps


def counter(my_func):
    @wraps(my_func)
    def inner(*args, **kwargs):
        inner.count += 1
        return my_func(*args, **kwargs)
    inner.count = 0
    return inner


@counter
def i_tell_you_what():
    return 'i tell you what'


i_tell_you_what()
i_tell_you_what()
print(f'{i_tell_you_what.__name__} run {i_tell_you_what.count} times')
# i_tell_you_what run 2 times

# make a cache with a default return dictionary as an arg

def cache_with_default(dct=None):
    if dct is None:
        dct = {}

    def cache(my_func):
        @wraps(my_func)
        def wrapper(*args):
            if args in dct:
                return dct[args]
            result = my_func(*args)
            dct[args] = result
            return result
        return wrapper
    return cache

# beware: use "()" in @cache_with_default() even when  no default args are passed in,  that takes you go to the depper level, into the wrapper func

@cache_with_default({(1,): 100})  # be careful, pass 1 as a tuple (1,) or it wont work.becaues the args will be (1,)
def times_two(x):
    return x + x


print(times_two(1))  # get 100 inside of 2 , because it was looked up in the dct


# Brett Slatkin - How to Be More Effective with Functions - PyCon 2015 - YouTube
# http://www.informit.com/articles/article.aspx?p=2314818

# keword_only_args:forced to be clear.
# dont pass infinity generator into *args, like itertools.count().it will try to tuple(count()),and that will crash.
# To avoid this possibility entirely, you should use keyword-only arguments when you want to extend functions that accept *args
# *this is a kwargs_only function, so :'anything after a "*" or "*args"  is FORCED to be clear (keyword)'


def kwargs_only(*args, a=1): #this a is forced to be clear, because a is after a "*"
    print(a)
    print(args)


kwargs_only(2, 2, 2, 2, a=4)
# 4
# (2, 2, 2, 2)

def bobby(*, propane=True, charcoal=False):
    # it nice to be clear, when your args are the same type data.
    if propane:
        print('I sell propane and propane accessories')
    else:
        print('the hell you say')


try:
    bobby(True, False)
except Exception as e:
    print(e)  # bobby() takes 0 positional arguments but 2 were given

bobby(propane=True, charcoal=False)  # I sell propane and propane accessories
#same idea , if you can ,put return value into a namedtuple inside of a tuple ,to be clear.--> 'Raymond Hettinger's Transforming Code into Beautiful, Idiomatic Python'
# use namedtuple as return tuple for clarity
from collections import namedtuple
def twitter_search(name,*,retweets=True,numtweets=0,popluar=False):
    twsearch=namedtuple('twsearch',['name','retweets','numtweets','popluar'])
    result=twsearch(name,retweets,numtweets,popluar)
    return result
obama=twitter_search('obama',retweets=False,numtweets=10,popluar=True)
print(obama)#twsearch(name='obama', retweets=False, numtweets=10, popluar=True)



# what is generator?
# iter(foo) is iter(foo)
# base on the talk-->Brett Slatkin - How to Be More Effective with Functions
# if iter(foo) is iter(foo):
#       now,then =itertools.tee(foo,2)
# customize iteration : "Brett Slatkin - How to Be More Effective with Functions - PyCon 2015 - YouTube" + "Loop like a native_ while, for, iterators, generators" ---->by using class __iter__ method:
# compare this info_get function and Info_Gen Class:
# difference is ever time you call the 'for' , __iter__method on class, it return a new iterator over a container.
# so far I prefer itertools.tee ,it is easier.
def info_gen(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        for line in reader:
            del line['Year']
            yield line


class Info_Gen:
    def __init__(self, path):
        self.path = path
        print(self.path)

    def __iter__(self):
        return info_gen(self.path)  # important must be returned ! to a genator func ,i believe it is the scope reason, if not returned, values are not catched.


# http://nvie.com/posts/iterators-vs-generators/   -----> "iter(iterable)-->iteration"
# how to detect a generator

lst = [1, 2, 3]
a = iter(lst)
b = iter(lst)
print(a is b)  # False
print(a == b)  # false
print([a] == [b])  # false
print(list(a) == list(b))  # true
c = iter(a)
print(a is c)  # True
print(a == c)  # True
print([a] == [c])  # false

lst = [1, 2, 3]
a = iter(lst)
c = iter(a)
print(list(a) == list(c))  # False  ([1,2,3] ==[])
# print(list(a))
# print(list(c))
# so if iter(foo) is iter(foo), foo is a generator; if iter(foo) is not iter(foo), foo is a container. 'iter over a iterator returns itself.'
# that is 'is' how about '=', how about [a],[b],[c] and list(a),list(d),list(c),see above.(this how i see it)basiclly, python doesn't look inside a iterator see what value it carry(and it shouldn't),so if 2 iterator object with different address, it is not equal(you can see as not 'is' ,so not '='). same thing with [],but list() is different. list() will really loop up the value.


# how does generator function(yield) run?

import contextlib


def HYW():
    print('hello')
    yield
    print('world')


a = HYW()  # Nothing happend, ! hello was not printed.
next(a)  # ---> now hello was printed. so when you call next, generator will run till it hits a yield

with contextlib.suppress(StopIteration):
    next(a)  # -----> world was printed, and then it hits the StopIteration





#  Ned Batchelder - Facts and Myths about Python names and values - PyCon 2015
# "reassign one of the name ,brother,doesnt reassign the other" ---Ned

a = [1, 2, 3]
b = a
a += [4, 5]  # what happened here unline is "a.extend([4,5]) and a =a "
print(b)  # -->[1, 2, 3, 4, 5]

a = [1, 2, 3]
b = a
a = a + [4, 5]
print(b)  # -->[1, 2, 3]

a = [1, 2, 3]
b = a
a.extend([4, 5])
print(b)  # -->[1, 2, 3, 4, 5]

a = [1, 2, 3]
b = a
a = a.extend([4, 5])
print(a)  # None
print(b)  # [1, 2, 3, 4, 5]

a = [1, 2, 3]  # try to make a =[10,20,30]
for x in a:
    x = x * 10
print(a)  # [1, 2, 3] failed:) beacuse a[0]still is 1 . the right way ,a=[x*10 for x in a]

nums = [1, 2, 3]
print(nums.__iadd__([4, 5]))  # [1, 2, 3, 4, 5],inplace and return the new value
print(nums) #[1, 2, 3, 4, 5]
print(nums.extend([7, 8]))  #print None. inplace but no return value,so print None
print(nums) #[1, 2, 3, 4, 5, 7, 8]




nums = [1, 2, 3]

def modify():
    print(nums)
    nums.append(4)

modify()  # [1, 2, 3, 1]

def re_assign():
    print(nums)
    nums += [5]
    # num=list.__iadd__(nums,[5]) this is modify first then re_assign,wont work for the assign part.

try:
    re_assign()
except Exception as e:

    print(e)  # local variable 'nums' referenced before assignment# csv.DictWriter fieldnames doesn't have to in order as the original DictReader, but all fieldnames have to be there.to modify del reader['keys']before write to writer


# "Fact: Python passes function arguments by assigning to them."means when you call a function, you assign the parameter to the "value" of the arg.
# @nedbatchelder.com
# Let’s examine the most interesting of these alternate assignments: calling a function. When I define a function, I name its parameters:
# def my_func(x, y):
#     return x+y
# Here x and y are the parameters of the function my_func. When I call my_func, I provide actual values to be used as the arguments of the function. These values are assigned to the parameter names just as if an assignment statement had been used:
# When my_func is called, the name x has 8 assigned to it, and the name y has 9 assigned to it. That assignment works exactly the same as the simple assignment statements we’ve been talking about. The names x and y are local to the function, so when the function returns, those names go away. But if the values they refer to are still referenced by other names, the values live on

# https://nedbatchelder.com/text/names.html
def a_func(num):
    num = num + 2


num = 2
num = a_func(num)

print(num)  # - - > None , in that function , local num was asign to the value of global num ,which is 2,and  local var num assign to 4(2+2) , now we return the func. and global num assign to nothing :None. local num 4 was no accessable in the global scope.


# ITERATION
# a trick  zip(*[iter(s)]*n)
lst = range(10)#[0,1,2,3,4,5,6,7,8,9]
print(iter(lst) is iter(lst))  # False
print(list(zip(*[iter(lst)] * 3)))  # [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
import itertools
print(list(itertools.zip_longest(*[iter(lst)]*3))) #[(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, None, None)]
# https://stackoverflow.com/questions/2233204/how-does-zipitersn-work-in-python
# zip(*lst) is funny
# [a]*n=[a,a,a,a,a....,a],same object a. so in this case [iter(lst)]*3 is != [iter(lst),iter(lst),iter(lst)],becasue three iter(lst) are 3 different objects.if you have to:a=iter(lst),then [iter(lst)]*3 =[a,a,a],By the way, range is not iterator.so iter(lst) is Not iter(lst),
# but map is a iterator.see below:
# https://stackoverflow.com/questions/16425166/accumulate-items-in-a-list-of-tuples

# try to make lst = [(0, 0), (2, 3), (4, 3), (5, 1)] into new_lst = [(0, 0), (2, 3), (6, 6), (11, 7)]
lst = [(0, 0), (2, 3), (4, 3), (5, 1)]

import itertools
new_lst = zip(*lst)  # zip_object contains ((0,2,4,5),(0,3,3,1))
new_lst = map(itertools.accumulate, new_lst)  # map_object contains ((0,2,6,11),(0,3,6,7))
# print(iter(new_lst) is iter(new_lst)) #True ,so map is a iterator
new_lst = list(zip(*new_lst))
print(new_lst)  # [(0, 0), (2, 3), (6, 6), (11, 7)]
# so all in one line: list(zip(*map(itertools.accumulate,zip(*lst))))

# itertools
# islice doesn't  consume the original iterator until next is called. most(all) itertools are like that.

# from itertools doc
from collections import deque


def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    if n is None:
        deque(iterable, maxlen=0)
    else:
        # itertools.islice(iterator,n,n) # THAT IS A NONO!!! islice doesn't  consume the original iterator  until Next is called!!!!!
        next(itertools.islice(iterator, n, n), None)  # YES


def tail(n, iterable):
    "Return an iterator over the last n items"
    # tail(3, 'ABCDEFG') --> E F G
    return iter(collections.deque(iterable, maxlen=n))


# cycle+compress, wanted a serial condition ,say one False and 20 True, forever
iterable = range(45)
result = itertools.compress(iterable, itertools.cycle(range(21)))  # 1-20,22-41,43,44

# itertools.repeat take container, not iterator. won't work.use repeat(tuple(iterator)).while cycle takes iterators.


# @accumulate usage: turn [1,2,3] in to int 123. or reduce
lst = [1, 2, 3]
result = itertools.accumulate(lst, lambda a, b: 10 * a + b)
print(list(result))  # [1, 12, 123]
# or use reduce , it is actually better
from functools import reduce
result = reduce(lambda a, b: 10 * a + b, lst)
print(result)  # 123

# takewhile,dropwhile,iter(callable func, sentinel(break) value);they works for <,>,=; to read a file by 32 characters -->iter(partial(f.read,32),'') see 'Transforming Code into Beautiful, Idiomatic Python'
# get all the fib nums  < 40,000
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]


def fib():
    a, b = 0, 1
    #unpacking seqiences,high level of thinking._R.H
    while True:
        yield a
        a, b = b, b + a


result = itertools.takewhile(lambda x: x < 40000, fib())  # right,or you can use generator expression+break func()

# or:

def breakfunc():
    'for generator seeing StopIteration will automaticlly break loop'
    raise StopIteration


result_2 = (x if x < 40000 else breakfunc() for x in fib())
print(list(result) == list(result_2))  # this also works


# groupby+defaultdict
# groupby :Itertools.groupby: 2 things need to point out, they are 1“the iterable needs to already be sorted on the same key function”. 2 “the source is shared, when the groupby() object is advanced, the previous group is no longer visible.” _doc
# it returns a tuple (key,A:iterator of the items that match the key)since this iterator shares the data of the groupby return value.when we iter over the return tuple, we need to capture the returned  A value right away.
# the standard  way will be to use “for key ,items in return_value: print key , list(items)”. so the problem I had before is I used the list()
"""Must get the value right away!
for key , items in groupby:
    use for loop store the items value into container.like :list or dictionay.most common way is list(items), you can use more complex as well.
    see """
# https://stackoverflow.com/questions/3749512/python-group-by
input = [('11013331', 'KAT'), ('9085267', 'NOT'), ('5238761', 'ETH'), ('5349618', 'ETH'), ('11788544', 'NOT'), ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('9843236', 'KAT'), ('5594916', 'ETH'), ('1550003', 'ETH')]
# result = [
#            {
#              type:'KAT',
#              items: ['11013331', '9843236']
#            },
#            {
#              type:'NOT',
#              items: ['9085267', '11788544']
#            },
#            {
#              type:'ETH',
#              items: ['5238761', '962142', '7795297', '7341464', '5594916', '1550003']
#            }
#          ]
from operator import itemgetter
input = sorted(input, key=itemgetter(1))
result = itertools.groupby(input, key=itemgetter(1))
# for key, items in result:
#     print(f'{key}--->{list(items)}')

# TH--->[('5238761', 'ETH'), ('5349618', 'ETH'), ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('5594916', 'ETH'), ('1550003', 'ETH')]
# KAT--->[('11013331', 'KAT'), ('9843236', 'KAT')]
# NOT--->[('9085267', 'NOT'), ('11788544', 'NOT')]
result = [{'type': key, 'items': [x for x, y in items]} for key, items in result]
import json
result = json.dumps(result, indent=2)
print(result) #yes

# now same thing again, with defaultdict
input = [('11013331', 'KAT'), ('9085267', 'NOT'), ('5238761', 'ETH'), ('5349618', 'ETH'), ('11788544', 'NOT'), ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('9843236', 'KAT'), ('5594916', 'ETH'), ('1550003', 'ETH')]
from collections import defaultdict
result=defaultdict(list)
for num,key in input:
    result[key].append(num)
# print(result)
# defaultdict(<class 'list'>, {'KAT': ['11013331', '9843236'], 'NOT': ['9085267', '11788544'], 'ETH': ['5238761', '5349618', '962142', '7795297', '7341464', '5594916', '1550003']})
result=[{'type': key, 'items':items} for key,items in result.items()]
result = json.dumps(result, indent=2)
print(result)#works too.

# another funny thing about groupby
# from [1,1,1,1,1,3,3,4,2,2,1,1,1,3,3] get[{1: 5}, {3: 2}, {4: 1}, {2: 2}, {1: 3}, {3: 2}]
lst=[1,1,1,1,1,3,3,4,2,2,1,1,1,3,3] #without sorting
result=itertools.groupby(lst)
# for key,items in result:
#     print(key,'--->',list(items))
# 1 ---> [1, 1, 1, 1, 1]
# 3 ---> [3, 3]
# 4 ---> [4]
# 2 ---> [2, 2]
# 1 ---> [1, 1, 1]
# 3 ---> [3, 3]
result=[{key:len(list(items))}for key ,items in result]
#if you only use {key:len(list(items))} ,you will get your result updated.you will get {1: 3, 3: 2, 4: 1, 2: 2}

print(result) #[{1: 5}, {3: 2}, {4: 1}, {2: 2}, {1: 3}, {3: 2}]

from collections import Counter
lst=[1,1,1,1,1,3,3,4,2,2,1,1,1,3,3]
result=Counter(lst)
print(result) #Counter({1: 8, 3: 4, 2: 2, 4: 1})
print(result.most_common(2))#[(1, 8), (3, 4)]

# some from Codingbat

# http://codingbat.com/prob/p118406
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.
def make_bricks(small, big, goal):
  return small+5*big>=goal and (goal-small)//5<=big and goal%5<=small

# http://codingbat.com/prob/p167025
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
    nums=nums+[0]#important
    result=[num for index,num in enumerate(nums) if not num==13 and nums[index-1]!=13]
    return sum(result)

# http://codingbat.com/prob/p186048
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  str=str+' ' #important !'eaacow'
  result=[x for index,x in enumerate(str) if x=='e' and str[index-2]=='o' and str[index-3]=='c' ]
  return len(result)


# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

# the logic of this problem is the highlight
def xyz_there(str):
  str=str.replace('.xyz','wwww')# important can not do replace('.xyz','').
  return 'xyz' in str



"the Great Raymond Hettinger's  Section"
#Transforming Code into Beautiful, Idiomatic Python + Python Class Toolkit
# iter(callable_func,sentinel_value)
# blocks=[]
# for block in iter(functools.partial(f.read,32),''):
#     blocks.appem=nd(block)
#
# for loop ,else:no break
dct= {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
# 'for key in dct' vs 'for key in list(dct)' --->when you are mutating the dictionary.

# "if you mutating something while you iter over it, you are living in the state of sin, and you deserve whatever happens to you"
# list is ever worse, make sure you don't do that,just make a new list.-->[x for index,x in enumerate(lst) if index%2==0]

try :
    for k in dct:
        if k.startswith('r'):
            del dct[k]
except Exception as e:
    print(e) #dictionary changed size during iteration


for key in list(dct):
    if key.startswith('r'):
        del dct[key]
print(dct) # {'matthew': 'blue'} --->works

dct= {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
while dct:
    key,value = dct.popitem()
    print(f'I just popped {key}---->{value}')
# I just popped raymond---->red
# I just popped rachel---->green
# I just popped matthew---->blue


# defaultdict for counting (collections.Counter), grouping(itertools.groupby



colors = ['red', 'green', 'red', 'blue', 'green', 'red']

# defaultdict
from collections import defaultdict
result=defaultdict(int)
for color in colors:
    result[color]+=1
print(result) #defaultdict(<class 'int'>, {'red': 3, 'green': 2, 'blue': 1})

# use Counter
from collections import Counter
result=Counter(colors)
print(result)#Counter({'red': 3, 'green': 2, 'blue': 1})

# use nothing(get)
result={}
for color in colors :
    result[color]=result.get(color,0)+1
print(result) #{'red': 3, 'green': 2, 'blue': 1}

#group

#defaultdict
names = ['raymond', 'rachel', 'matthew', 'roger','betty', 'melissa', 'judith', 'charlie']
result_1=defaultdict(list)
for name in names:
    key=len(name)
    result_1[key].append(name)
print(result_1)
#defaultdict(<class 'list'>, {7: ['raymond', 'matthew', 'melissa', 'charlie'], 6: ['rachel', 'judith'], 5: ['roger', 'betty']})

#use get
result_2={}
for name in names:
    key=len(name)
    result_2[key]=result_2.get(key,[])+[name]#be careful, don't use append, becauese it returns nothing,result_2[key] will be None
print(result_2)
# {7: ['raymond', 'matthew', 'melissa', 'charlie'], 6: ['rachel', 'judith'], 5: ['roger', 'betty']}


#groupby
import itertools
result_3=sorted(names,key=len)
result_3=itertools.groupby(result_3,key=len)
# for key,names in result_3:
#     print(key,'--->',list(names))
# 5 ---> ['roger', 'betty']
# 6 ---> ['rachel', 'judith']
# 7 ---> ['raymond', 'matthew', 'melissa', 'charlie']
result_3={key:list(names) for key,names in result_3}
print(result_3)
# {5: ['roger', 'betty'], 6: ['rachel', 'judith'], 7: ['raymond', 'matthew', 'melissa', 'charlie']}

"Linking dictionaries" 'ChainMap'
defaults = {'color': 'red', 'user': 'guest'}
envir={'user':'frank','login':'Unknown'}
command={'login':True}
from collections import ChainMap
result=ChainMap(command,envir,defaults) #high to low
print(result['color'])#red
print(result['login'])#True
print(result['user'])#frank




from functools import wraps
# famous cache decorator
def cache(my_func):
    saved={}
    @wraps(my_func)
    def wrapper(*args):
        if args in saved:
            print('returned from saved')
            return saved[args]
        result=my_func(*args)
        saved[args]=result
        print('return from func(*args)')
        return result
    return wrapper

@cache
def printer(a):
    print(a.upper())
printer('a')
# A
# return from func(*args)
printer('a')
# returned from saved

# this is realy a bad example,because second time 'A' was not printed.so it doesn't not work for all functions.

@cache
def rt(a):
    return a.upper()
print(rt('a'))
# return from func(*args)
# A
print(rt('a'))
# returned from saved
# A
# works good this time:)

# the setup,teardown in sqlite "with conn"
with contextlib.suppress(Exception):#since we have no database working now
    with conn:
        cur = conn.cursor()
        cur.execute( ... )

# The patch contextmanager, this testing code is from CoreyMSchafer--> https://github.com/CoreyMSchafer
import requests

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

# and another module :
import unittest
# from employee import Employee
from unittest.mock import patch
class TestEmployee(unittest.TestCase):
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

# if __name__=='__main__':
    # unittest.main()



"Python's Class Development Toolkit _ Raymond Hettinger"
#"Python is consenting as an adult language. We don't leave the locks on the door." _ Raymond Hettinger

"""
Circles, Inc.
"""


class Circle:  # python 3 is automatically a new style class. 2.7 needs to inherit (object)
    from math import pi
    """An advvanced circle analytics toolkit"""
    # don/t skip the elevator pitch ,your doc string.
    # what is inside a class is effectlly a module ,it is like the code run in its own module.

    print('i am defining a class')  # it will print only by defining it.
    # raymond also talked about you can open file or for loop with in the class.

    version = '0.1'  # class variable for shared data,while instance var for unique data. use str, or tuple
    print('dont use bi_floats , try:0.1+0.7,you will get ', 0.1 + 0.7)  # 0.7999999999999999

    def __init__(self, radius):
        # "__init__ " is not a constructor. is calling the class construct a instance.__init__ is 'poplulate' instance variable.
        # one thing is for sure, user is gonna make lots of instance, i mean a lot .
        print('i am running __init__')
        self.radius = radius

    def area(self):
        return self.radius**2 * pi
    # so far we are good to go, more method ? until user ask for it! before that,YAGNI:) Lean startup.


# First customer: Academia
# from random import random, seed
# seed(8675309)
# print 'Using Circuituous(tm) version', Circle.version
# n = 10
# circles = [Circle(random()) for i in xrange(n)]
# print 'The average area of', n, 'random circles'
# avg = sum([c.area() for c in circles]) / n
# print 'is %.1f' % avg
# print

    def perimeter(self):
        # new customer wants a perimeter method.
        return self.radius * 2 * pi

# Second customer: Rubber sheet company
# cuts = [0.1, 0.7, 0.8]
# circles = [Circle(r) for r in cuts]
# for c in circles:
#     print 'A circlet with with a radius of', c.radius
#     print 'has a perimeter of', c.perimeter()
#     print 'and a cold area of', c.area()
#     c.radius *= 1.1
#     print 'and a warm area of', c.area()
#     print


# this customer changed the attribute "c.radius *= 1.1"
"if it is a variable, it is gonna change, sooner or later"  # R.H

# If you expose an attribute, expect users to all kinds of interesting things with it.


# 3rd customer Tire
class Tire(Circle):
    'Tires are circles with a corrected perimeter'
    # again
    "if it is a variable, it is gonna change, sooner or later"  # R.H


def perimeter(self):
    'Circumference corrected for the rubber'
    return Circle.perimeter(self) * 1.25


# t = Tire(22)
# print 'A tire of radius', t.radius
# print 'has an inner area of', t.area()
# print 'and an odometer corrected perimeter of',
# print t.perimeter()
# print


# Next customer: Na;onal graphics company
# bbd = 25.1
# c = Circle(bbd_to_radius(bbd)
# print 'A circle with a bbd of 25.1'
# print 'has a radius of', c.radius
# print 'an an area of', c.area()
# print

# c = Circle(bbd_to_radius(bbd)) -------> this is Baaaad!
'USE Alternative Constructor'
print(dict.fromkeys(['name', 'age', 'language']))
#{'name': None, 'age': None, 'language': None}

# /lets go back and add the alternative constructor

import math


class Circle:

    'An advanced circle analytic toolkit'
    version = '0.3'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod
    # classmethod make sure you use cls , for the subclass usage
    def from_bbd(cls, bbd):
        radius = bbd / 2.0 / math.sqrt(2.0)
        # return Circle(radius) NONO!
        # classmethod make sure you use cls , for the subclass usage
        return cls(radius)


c = Circle.from_bbd(25.1)
# print 'A circle with a bbd of 25.1'
# print 'has a radius of', c.radius
# print 'an an area of', c.area()
# print

# New customer request: add a func
# use staticmethod ,a giveaway is your func does not need 'self' or 'cls'. you use staticmethod for the findability of your func.


class Circle(object):
    'An advanced circle analytic toolkit'
    version = '0.4'

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    # attach functions to classes to increase the findability of your func.
    # a giveaway is your func does not need 'self' or 'cls'.
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


# Government request: ISO-11110: "you need to use perimeter to calc the area" ,like this:

# class Circle(object):
#     'An advanced circle analytic toolkit'
#     version = '0.5b'
#     def __init__(self, radius):
#             self.radius = radius
#     def area(self):
#         p = self.perimeter()
#         r = p / math.pi / 2.0 return math.pi * r ** 2.0
#     def perimeter(self):
#         return 2.0 * math.pi * self.radius


# that wasnot too bad,really?
# the Tire subclass update the perimeter, now you broke their code.

# class Tire(Circle):
#     'Tires are circles with an odometer corrected perimeter'
# def perimeter(self):
# 'Circumference corrected for the rubber' return Circle.perimeter(self) * 1.25


'so what to do?'  # normally 'self' means you or your children.in this case. self.perimeter(). means if tire class has this method.it will not look up to the mother class.So you want to make 'self' means you Only ------>local reference.
# the idea is to  use classname+methodname.
# __perimeter---> Name mangling into---> '_(class.__name__)__perimeter'


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * math.pi

    # make local refernce perimeter
    __perimeter = perimeter

    # see Ned Batchelder - Facts and Myths about Python names and values - PyCon 2015
    # a=3
    # b=a
    # a=4
    # print(b)---->3

    def area(self):
        p = self.__perimeter()
        r = p / (2 * math.pi)
        return math.pi * r**2


# Government request: ISO-22220
# •  You’re not allowed to store the radius
# •  You must store the diameter instead!

# we get to keep the api the same. still i accept radius in __init__, but diameter will be stored instead.


# it breaks our entire class!
#" I just wish everytime i use dot for look up,            it will magiclly trans into a get method call ()"
#" I just wish everytime I set a radius(even in __init__) ,it will magiclly trasn in to s set radius call,--store the diameter."
# yes, this is the @property .But dont do it just for it.dot look up and '=' assign is much easier."if you find yourself design a setter and getter,you probably doing it wrong"
# property is for "after the fact , that you dont need to change any existing code.and add on the property"


# User request: Many circles
# n = 10000000
# seed(8675309)
# print 'Using Circuituous(tm) version', Circle.version
# circles = [Circle(random()) for i in xrange(n)]
# print 'The average area of', n, 'random circles'
# avg = sum([c.area() for c in circles]) / n
# print 'is %.1f' % avg
# print
# I sense a major memory problem.
# Circle instances are over 300 bytes each!

'Flyweight design paUern: Slots'
# save this for the last.you cant add new attr ,you cant access the dictinary no more.no vars() or .__dict__.
# "from the user view, there are no changes at all"_R.H
# dont worry ,subclass does not inherit the slots


class Circle(object):

    'An advanced circle analytic toolkit'
# flyweight design pattern suppresses
# the instance dictionary
    __slots__ = ['diameter']
    version = '0.7'

    def __init__(self, radius):

        self.radius = radius

    @property  # convert dotted access to method calls
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0


"""Summary: Toolset for New - Style Classes
1.  Inherit from object().
2.  Instance variables for informa
on unique to an instance.
3.  Class variables for data shared among all instances.
4.  Regular methods need “self” to operate on instance data.
5.  Thread local calls use the double underscore. Gives subclasses the freedom to override methods without breaking other methods.
6.  Class methods implement alterna
ve constructors. They need “cls” so they can create subclass instances as well.
7.  Sta
c methods aUach func
ons to classes. They don’t need either “self” or “cls”. Sta
c methods improve discoverability and require context to be specified.
8.  A property() lets geUer and seUer methods be invoked automa
cally by aUribute access. This allows Python classes to freely expose their instance variables.
9.  The “__slots__” variable implements the Flyweight Design PaUern by suppressing instance dic
onaries."""


# from until_mar_29.py
# classmethod always use cls for subclass
#__repr__ usage
#__from_string__usage, if string contain classname then: classname,*info=info_string.split(' ')


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @classmethod
    def from_str(cls, info_string):
        return cls(*info_string.split(' '))

    def __repr__(self):
        return f'{self.__class__.__name__}{tuple(vars(self).values())}'


emp_1 = Employee.from_str('frank young')
print(emp_1)



'THANKS TO Corey Schafer,Ned Batchelder,Thomas Ballinger,Brett Slatkin,and The Great Raymond Hettinger'



# Other modules on the side:pytz, re(Regular expression), logging, bs4.BeatifulSoup, sqlite3, basic terminal operations.



#
#
#
# From May_14:
# I have problem you might want to try:  Many web pages ask for the telephone number.  Many times the interface is very picky and one needs to put it the numbers separated by -'s: 512-123-4567; other times, they want no -'s:  5121234567.  Can you write a Python program so that if I input any of the following strings, the number is accepted and displayed as (512) 123-4567 or an error is produced?
# RE

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
    else:
        print(f'error! {num}')

# another thing: finditer returns a iterator, wheather there is a match or not, it will return a iterator.I guess the same philosophy apply to all func returns iterator,because the value has not been looked up yet.so they dont even know if there is a value.

# for number in numbers.split('\n'):

#     matches = pattern.finditer(number)
#     if not mathce: (this wont work , because it always return a iterator ,like iter([]))
#     so do this:
#     if not list(matches):
#         'but you consumed the iterator ,so best practice is use findall,if else'
#         print(f'{number} is bad')
#       512 l23 4567  (expect error) is bad
#       (512) 12E 4567  (expect error) is bad
#       (512) 123 456  (expect error) is bad
