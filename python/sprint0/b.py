from typing import List, Tuple

"""
Даны два массива чисел длины n. Составьте из них один массив длины 2n, 
в котором числа из входных массивов чередуются 
(первый — второй — первый — второй — ...). 
При этом относительный порядок следования чисел из одного массива должен 
быть сохранён.
"""


def zipper(a: List[int], b: List[int]) -> List[int]:
    """"""
    n = len(a)
    res = []
    for i in range(0, n):
        res.append(a[i])
        res.append(b[i])

    return res


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
