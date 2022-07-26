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
cdabra
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


def prev(node, idx):
    while idx:
        node = node.next_item
        idx -= 1
    return node


def solution(node, idx):
    if idx == 0:
        next = node.next_item
        return zas(next)
    previous_node = prev(node, idx-1)
    previous_node.next_item = previous_node.next_item.next_item
    zas(node)


def zas(node):
    # !!!
    while node is not None:
        print(node.value)
        node = node.next_item


def zas(node):
    if node.value is not None:
        print(node.value)
        while node.next_item is not None:
            node = node.next_item
            print(node.value)


def create_list():
    count = int(input())

    node = None
    for _ in range(count):
        value = input()
        node = Node(value, next_item=node)

    return node


def create_list_local():
    node = None

    for x in ['a', 'b', 'c']:
        value = x
        node = Node(value, next_item=node)

    return node


if __name__ == '__main__':
    # Обрати внимание, создание списка.
    head = create_list()
    # head = create_list_local()

    # Индекс элемента для удаления.
    inx_delete = int(input())
    # inx_delete = 0

    # Твоя функция.
    solution(head, inx_delete)
