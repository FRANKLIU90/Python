def make_printer(msg):
    def printer():
        print(msg)
    return printer


make_printer('hrllo')()
make_printer('mahis')()


def multipliers():
    return [lambda x: i * x for i in range(4)]


result = [m(2) for m in multipliers()]
print(result)


result = (m(2) for m in multipliers())

for x in result:
    print(x)


ms = [lambda x: x * i for i in range(4)]
result = [m(2) for m in ms]
print(result)
result = (m(2) for m in ms)
for x in result:
    print(x)
msg = (lambda x: x * i for i in range(4))
# result = [m(2) for m in msg]
# print (result)
print('jaj')
result = (m(2) for m in msg)
for x in result:
    print(x)


def gret(num):
    x = num**2

    def sf():
        print(x)
    return sf


m = gret(10)
n = gret(5)
m()
n()
