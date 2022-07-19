"""
Нелюбимое дело

Создать однонаправленный список Node.
Заполнить его.
Написать функцию для удаления элемента по индексу.
Вывести на экран, начиная с головы списка.

Пример.

input
4
abra
ca dabra
boom
oops
0

output:
boom
ca dabra
abra

"""


class Node:
    """Однонаправленный список."""
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, index_for_delete):
    # Your code
    ...


if __name__ == '__main__':
    count = int(input())

    # Создание однонаправленного списка.
    node = None
    head = None
    for _ in range(count):
        value = input()
        node = Node(value, next_item=node)
        if head is None:
            head = node

    # Вывод списка.
    solution(node)
