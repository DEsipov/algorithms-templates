#!-*-coding:utf-8-*-
"""Реализация с chunk."""

CHUNK = 50


def reload(lst, k):
    lst_ord = sorted(lst)[:k]
    del lst
    return sorted(lst_ord)[:k]


def calc(lst, k):

    res = []
    max_item = None

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            item = abs(lst[i] - lst[j])

            if max_item is None:
                res.append(item)
            elif item < max_item:
                res.append(item)

            if len(res) == CHUNK:
                res = reload(res, k)
                max_item = res[-1]

    res = reload(res, k)
    return res[k - 1]


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
    # n = 3
    # line = '9 6 10 3'
    # k = 3
    # expected = 3

    # Для отправки.
    n = int(input())
    line = input()
    k = int(input())

    lst = tuple(map(int, line.split()))

    res = calc(lst, k)
    print(res)
    # print(f'res: {res}')
