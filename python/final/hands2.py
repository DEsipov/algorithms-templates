import collections


def juggle(keys_count, matrix, number_players=2):
    # Лучше все равно не загромождать.
    cnt = collections.Counter(matrix)
    # Почитай про обход словаря в цикле.
    # Здесь создаем, грубо говоря, список [1, 1], а потом считаем сумму его
    # элементов.
    # почитай про генераторы списков, но в sum можно опустить квадратные скобки
    return sum(v <= keys_count * number_players for v in cnt.values())


def calc():
    # Для тестов, так удобнее делать.
    k = 3
    # Можно точки заранее убрать из строки.
    line = '12312..22..22..2'.replace('.', '')
    # Можно перенести условие в начале и тогда получим список
    # [True, False, True], а это идентично [1, 0, 1]
    res = sum(
        k * 2 <= line.count(str(x)) and line.count(str(x))
        for x in range(1, 10)
    )
    print(res)



if __name__ == "__main__":
    # k = int(input())
    # # Хитро! Идея огонь! Можно через цикл сделать, если что.
    # line = f'{input()}{input()}{input()}{input()}'

    # Для тестов, так удобнее делать.
    k = 3
    # Можно точки заранее убрать из строки.
    line = '12312..22..22..2'.replace('.', '')
    print(juggle(k, line))
