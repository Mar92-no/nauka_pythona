# def print_dict(dict):
#     for key in dict:
#         print("{0}: {1}" .format(key, dict[key]))
#
# if __name__ == '__main__':
#     print('tu jestem')
#     samolot = {'n': 'mig', 'przeb': 1220}
#     print_dict(samolot)
#
#
#     samolot['dlugosc'] = 10
#     print_dict(samolot)


def calculator(a, b, op):
    if op == '+':
        return a+b

    if op == '-':
        return a-b

    if op == '/':
        return a/b

    if op == '*':
       return a*b


if __name__ == '__main__':
    c = calculator(1,2,'+')
    print(c)
    d = calculator(1,2,'-')
    print(d)
    e = calculator(1,2,'/')
    print(e)
    f = calculator(1,2,'*')
    print(f)
