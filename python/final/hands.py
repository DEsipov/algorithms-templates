#!-*-coding:utf-8-*-

"""
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.
"""

# Кол-во клавиш, которые можно нажать.
from unittest import TestCase

NUM_COUNT = 9
SIGN = '.'
LINE_COUNT = 4


def generate_dict():
    return {str(k): 0 for k in range(1, NUM_COUNT + 1)}


def update_dict(line, dct):
    for x in line:
        if x == SIGN:
            continue

        dct[str(x)] += 1

    return dct


def calculate(dct: dict, k: int):
    res = 0
    for t in range(1, NUM_COUNT + 1):
        value = dct[str(t)]
        if value and int(value) <= int(k) * 2:
            res += 1

    return res


if __name__ == '__main__':
    dct = generate_dict()
    k = input()
    for _ in range(LINE_COUNT):
        line = input()
        update_dict(line, dct)

    res = calculate(dct, k)
    print(res)


class HandsTestCase(TestCase):

    def test_one(self):
        k = 3
        mtx = [
            '1231',
            '2..2',
            '2..2',
            '2..2',
        ]
        dct = generate_dict()
        for line in mtx:
            update_dict(line, dct)

        res = calculate(dct, k)

        expected = 2
        self.assertEqual(res, expected)

    def test_two(self):
        k = 4
        mtx = [
            '1111',
            '9999',
            '1111',
            '9911',
        ]

        dct = generate_dict()
        for line in mtx:
            update_dict(line, dct)

        res = calculate(dct, k)

        expected = 1
        self.assertEqual(res, expected)

    def test_three(self):
        k = 4
        mtx = [
            '1111',
            '1111',
            '1111',
            '1111',
        ]

        dct = generate_dict()
        for line in mtx:
            update_dict(line, dct)

        res = calculate(dct, k)

        expected = 0
        self.assertEqual(res, expected)