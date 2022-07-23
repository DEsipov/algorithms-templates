"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None.
При этом push(x) и pop() также должны выполняться за константное время.


Формат ввода
В первой строке записано одно число — количество команд,
оно не превосходит 100000. Далее идут команды по одной в строке.
Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class StackMax:

    def __init__(self):
        self.items = []
        self.head = None
        self.max_item = None

    def push(self, x):
        self.items.append(x)
        if self.max_item is None or x > self.max_item:
            self.max_item = x

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        return self.max_item


def run():
    stack = StackMax()
    stack.push(7)
    stack.push(8)
    stack.push(3)
    stack.push(9)
    stack.get_max()

    print('run')


if __name__ == '__main__':

    run()
