"""
Список дел

Создать однонаправленный список Node.
Заполнить его и вывести на экран, начиная с головы списка.

Пример.

input
3
abra
ca dabra
boom

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


def solution(node):
    while node is not None:
        print(node.value)
        node = node.next_item


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
