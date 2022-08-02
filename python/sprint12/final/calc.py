#!-*-coding:utf-8-*-


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

    def calculate(self):
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


if __name__ == '__main__':
    # line = local_get_line().split()
    line = get_input_line().split()
    calc = Calc(line)

    res = calc.calculate()
    print(res)
