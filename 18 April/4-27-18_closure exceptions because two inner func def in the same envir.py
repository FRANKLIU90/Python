def outer(a):
    i = 1

    def inner_1(b):
        return f'i:{i} b:{b}'
    i = 2

    def inner_2(b):
        return f'i:{i} b:{b}'
    result = [inner_1, inner_2]
    return result


w = outer('A')
for func in w:
    print(func('1'))
# inner_1 and Inner_2



def outer(a):
    i = 1

    def inner_1(b):
        return f'i:{i} b:{b}'
    yield inner_1
    i = 2

    def inner_2(b):
        return f'i:{i} b:{b}'
    yield inner_2
    # result = [inner_1, inner_2]
    # return result


w = outer('A')
for func in w:
    print(func('1'))
