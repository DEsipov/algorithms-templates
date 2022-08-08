#!-*-coding:utf-8-*-
"""Реализация с односвязным списком."""


class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value

    def __str__(self):
        return f'{self.value}'


class Tree:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def insert(self, value):
        # Первый элемент
        # print(f'val: {value}')
        if not self.head:
            new_node = Node(value)
            self.head = self.tail = new_node
            self.size += 1
            return

        # Есть свободные места.
        # if self.size < self.max_size:
        if True:
            # Вставка в начало.
            if value <= self.head.value:
                new_node = Node(value, next=self.head)
                self.head = new_node
                self.size += 1
            else:
                # Вставка далее.
                # 3 1 6 4
                # print(self.print_tree())
                cur = self.head
                prev = cur
                while cur.next is not None and cur.value < value:
                    prev = cur
                    cur = cur.next

                if cur.next is None and cur.value < value:
                    new_node = Node(value, next=cur.next)
                    cur.next = new_node
                else:
                    new_node = Node(value, next=cur)
                    prev.next = new_node

                self.size += 1

                if new_node.next is None:
                    self.tail = new_node
        else:
            # Все места заняты.
            pass

    def get_result(self):
        cur = self.head
        i = 1
        while i != k:
            cur = cur.next
            i += 1

        return cur.value

    def print_tree(self):
        cur = self.head
        lst = []
        while cur is not None:
            lst.append(cur.value)
            cur = cur.next

        # print('SiZE:', self.size, 'LST:', *lst)


def calc(lst, k):
    tree = Tree(max_size=k)

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            item = abs(lst[i] - lst[j])
            tree.insert(item)

    # print(tree.get_result())
    return tree.get_result()


if __name__ == '__main__':
    # Пример 1
    # n = 3
    # line = '1 3 5'
    # k = 3
    # expected = 4

    # Пример 2
    # n = 3
    # line = '1 3 1'
    # k = 1
    # expected = 0

    # Пример 3
    n =3
    line = '9 6 10 3'
    k = 3
    # expected = 3

    # Для отправки.
    # n = int(input())
    # line = input()
    # k = int(input())

    lst = list(map(int, line.split()))

    res = calc(lst, k)
    print(res)
    # print(f'res: {res}')
