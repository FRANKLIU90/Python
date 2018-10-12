import csv
# with open('random.csv') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for id, infos in enumerate(reader):
#         # print(id, str(infos)[1:-1])
#         # print(f'({id},{str(infos)[1:-1]})')
#         w = [f'({id},{str(infos)[1:-1]})' for id, infos in enumerate(reader)]
# print(','.join(w))
# with open('random.csv') as f:
#     a = next(f)
#     # a = '\n'.join(a)
#     # print(a.split(','))
#     a = a.split('","')

#     print('\n'.join(a))
#     # for id, infos in enumerate(f):
#     #     print(id, ',', infos, end='')
with open('random.csv') as f:
    a = next(f)[:-1]
    # print(a)
    for x in a.split(','):
        print(x[1:-1])

    for index, line in enumerate(f, start=1):
        line = line[:-1]
        print(f'({index},{line})', end=',')
# with open('random.csv') as f:
#     print(next(f))
#     for index, line in enumerate(f, start=1):
#         line = line[:-1]
#         print(f'({index},{line})',end=',')
