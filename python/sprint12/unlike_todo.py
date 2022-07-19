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


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next_item


def create_list():
    count = int(input())

    node = None
    head = None

    for _ in range(count):
        value = input()
        node = Node(value, next_item=node)
        if head is None:
            head = node

    return head


def get_node_by_index(node, index):
    """Получить элемент по индексу."""
    while index:
        node = node.next_item
        index -= 1
    return node


def remove_by_index(head, idx_delete):
    if idx_delete == 0:
        return get_node_by_index(head, idx_delete + 1)

    prev = get_node_by_index(head, idx_delete - 1)
    prev.next_item = prev.next_item and prev.next_item.next_item

    return head


if __name__ == '__main__':
    head = create_list()

    inx_delete = int(input())

    # Удаление.
    head = remove_by_index(head, inx_delete)
    # Вывод списка.Вывод списка.
    print_list(head)
