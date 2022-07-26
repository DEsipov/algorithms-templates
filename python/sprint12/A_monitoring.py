#!-*-coding:utf-8-*-

"""
Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.

Input
# 4
# 3

# 1 2 3
# 0 2 6
# 7 4 1
# 2 7 0

# Out
# 1 0 7 2
# 2 2 4 7
# 3 6 1 0

"""


def create_matrix():
    n = int(input())
    m = int(input())

    mtx = []
    for _ in range(n):
        line = list(input().split())
        mtx.append(line)

    return mtx, n, m


def print_matrix(mtx):
    for row in mtx:
        line = ' '.join(map(str, row))
        print(line)


def local_create_matrix():
    """Создает матрицу.

    Возвращает кортеж из матрицы, кол-ва ее строка и количества ее столбцов.
    """
    n, m = 4, 3
    mtx = [
        [1, 2, 3],
        [0, 2, 6],
        [7, 4, 1],
        [2, 7, 0],
    ]

    return mtx, n, m


def print_transpon_matrix(mtx, n, m):
    for i in range(m):
        # Во внешнем цикле обнуляем именно список, а не строку.
        row = []
        for j in range(n):
            row.append(mtx[j][i])

        # Выводим строку. Посмотри про метод join у строки.
        line = ' '.join(row)
        print(line)


if __name__ == '__main__':
    # Создания данных для отладки, чтоб руками не вводить.
    mtx, n, m = local_create_matrix()
    # Метод, в котором создается матрица из данных пользователя.
    # mtx, n, m = create_matrix()
    # Функция, которая печатает результат.
    print_transpon_matrix(mtx, n, m)
