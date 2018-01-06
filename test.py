'''
test.py
'''

import math

t = 123, 'abc', ['sadasdsad', 'sadasdasd']
print(type(t))


class TestClassMethod(object):
    METHOD = 'method hoho'

    def __init__(self):
        self.name = 'leon'

    def test1(self):
        print('test1')
        print(self)

    @classmethod
    def test2(cls):
        print(cls)
        print('test2')
        print(cls.METHOD)
        print('----------------')

    @staticmethod
    def test3():
        print(TestClassMethod.METHOD)
        print('test3')


def fibs(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    f = fibs(10)
    for i in f:
        print(i, end=', ')
