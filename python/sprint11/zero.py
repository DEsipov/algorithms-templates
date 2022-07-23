#!-*-coding:utf-8-*-
from unittest import TestCase


def get_forward_lst(lst):

    res = []
    d = len(lst)
    for n in lst:
        if n == 0:
            d = 0
        else:
            d += 1

        res.append(d)

    return res


def zeronear(lst):
    to_left = get_forward_lst(lst)
    to_right = tuple(reversed(get_forward_lst(list(reversed(lst)))))
    return list(map(min, zip(to_left, to_right)))


################### Для Ya ###################
# def read_input() -> Tuple[List[int], List[int]]:
#     n = int(input())
#     return list(map(int, input().strip().split()))
#
#
# lst = read_input()
# result = zeronear(lst)
# print(" ".join(map(str, result)))
################### Для Ya ###################


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


if __name__ == '__main__':
    ts = ZeroTestCase()
    ts.test_smoke_1()
    ts.test_smoke_2()
