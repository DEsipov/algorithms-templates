from typing import Tuple

"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу 
вывести их сумму, также в двоичной системе. 
Встроенную в язык программирования возможность сложения двоичных 
чисел применять нельзя. Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов 
максимального числа на входе.
 
 Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. 
Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.

Пример 1
Ввод
1010
1011
 
Вывод
10101

Пример 2
Ввод
1
1
 
Вывод
10
"""

TWO = 2


def get_sum(first_number: str, second_number: str) -> str:
    print('Input:', first_number, second_number)

    # Переворачиваем для удобства.
    a = first_number[::-1]
    b = second_number[::-1]

    n = max(len(a), len(b))

    buffer = 0
    result = []

    for i in range(n):
        # сложение в столбике.
        a_item = a[i] if i < len(a) else 0
        b_item = b[i] if i < len(b) else 0

        c = int(a_item) + int(b_item) + buffer
        result.append(str(c % TWO))

        # в уме.
        buffer = c // TWO

    if buffer:
        result.append(str(buffer))

    result.reverse()
    return ''.join(result)


def read_input() -> Tuple[str, str]:
    # first_number = input().strip()
    # second_number = input().strip()
    first_number = '101100'
    second_number = '1011'
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
