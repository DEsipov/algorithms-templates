#!-*-coding:utf-8-*-
"""Реализация с односвязным списком."""


def calc(lst, k):
    res = []

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            item = abs(lst[i] - lst[j])
            res.append(item)

    res = sorted(res)
    # print(res)
    return res[k - 1]


if __name__ == '__main__':
    # Пример 1
    n = 3
    line = '1 3 5'
    k = 3
    # expected = 4

    # Пример 2
    # n = 3
    # line = '1 3 1'
    # k = 1
    # expected = 0

    # Пример 3
    # n =3
    # line = '9 6 10 3'
    # k = 3
    # expected = 3

    # Для отправки.
    n = int(input())
    line = input()
    k = int(input())

    lst = list(map(int, line.split()))

    res = calc(lst, k)
    print(res)
    # print(f'res: {res}')
