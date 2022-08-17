#!-*-coding:utf-8-*-
from typing import Callable


class OperationError(Exception):
    pass


class Calc:

    OPERATIONS = '+-*/'

    def __init__(self, line):
        self.line = line
        self.stack = []

    def execute_operation(self, oper):
        y = int(self.stack.pop())
        x = int(self.stack.pop())

        if oper == '+':
            self.stack.append(x + y)
        elif oper == '-':
            self.stack.append(x - y)
        elif oper == '*':
            self.stack.append(x * y)
        elif oper == '/':
            self.stack.append(x // y)
        else:
            raise OperationError()

    def calculate(self, line):
        for x in line:
            if x in self.OPERATIONS:
                self.execute_operation(x)
            else:
                self.stack.append(x)

        return int(self.stack.pop())


def local_get_line():
    # return '7 2 + 4 * 2 +'
    # return '50 2 - 12 /'
    return '2 5 - 4 /'


def get_input_line():
    return input()


# Первый параметр - это функция.
def calc(operator: Callable, operand_x, operand_y):
    return operator(operand_x, operand_y)


if __name__ == '__main__':
    from operator import add

    x, y = 5, 17

    res = calc(operator=add, operand_x=x, operand_y=y)

    print(res)

