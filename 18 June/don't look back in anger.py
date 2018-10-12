def counter(my_func):
    def inner(*args, **kwargs):
        inner.counter += 1
        return my_func(*args, **kwargs)
    inner.counter = 0
    return inner


@counter
def md():
    return 'a'


md()
md()

md()
md()
print(md.counter)
