#!-*-coding:utf-8-*-

# Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет
# жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков.

# Каждый участок либо пустой, либо на нём уже построен дом.
# Общительный Тимофей не хочет жить далеко от других людей на этой улице.

# Поэтому ему важно для каждого участка знать расстояние до ближайшего
# пустого участка.

# Если участок пустой, эта величина будет равна нулю —
# расстояние до самого себя.

# Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть
# карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором
# строились, поэтому их номера на карте никак не упорядочены.
# Пустые участки обозначены нулями.


# Формат ввода
# В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей
# строке записаны n целых неотрицательных чисел — номера домов и
# обозначения пустых участков на карте (нули). Гарантируется,
# что в последовательности есть хотя бы один ноль. Номера домов
# (положительные числа) уникальны и не превосходят 109.

# Формат вывода
# Для каждого из участков выведите расстоя\ние до ближайшего нуля.
# Числа выводите в одну строку, разделяя их пробелами.

# Пример данных.
# n = 5
# lst = [0, 1, 4, 9, 0]
# res = [0, 1, 2, 1, 0]
import unittest
from typing import List, Tuple
from unittest import TestCase


def zeronear(lst):
    n = len(lst)
    forward = [0] * n
    backward = [0] * n
    for i in range(0, n):
        # forward
        j = i
        while lst[j] != 0:
            forward[i] += 1
            j += 1
            if j == n:
                forward[i] = n
                break

        # backward
        j = n - 1 - i
        while lst[j] != 0:
            backward[i] += 1
            j -= 1
            if j < 0:
                backward[i] = n
                break

    backward.reverse()
    return list(map(min, zip(forward, backward)))


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    return list(map(int, input().strip().split()))


lst = read_input()

result = zeronear(lst)
print(" ".join(map(str, result)))


class ZeroTestCase(TestCase):

    def test_smoke_1(self):
        input_data = [0, 1, 4, 9, 0]
        expected_data = [0, 1, 2, 1, 0]

        res = zeronear(input_data)

        self.assertEqual(expected_data, res)

    def test_smoke_2(self):
        input_data = [0, 7, 9, 4, 8, 20]
        # 0 7 9 4 8 20
        expected_data = [0, 1, 2, 3, 4, 5]

        res = zeronear(input_data)

        self.assertEqual(expected_data, res)


# if __name__ == '__main__':
#     ts = ZeroTestCase()
#     ts.test_smoke_1()
#     ts.test_smoke_2()



