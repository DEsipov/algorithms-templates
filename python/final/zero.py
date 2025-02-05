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

from python.tools import timer

lst = [0, 1, 4, 9, 0]
expected_res = [0, 1, 2, 1, 0]


@timer
def zeronear(lst):
    n = len(lst)
    res = []
    res2 = []
    for i in range(n):
        pos = 0
        pos2 = 0
        fl2 = True

        for j in range(i, n):
            if fl2:
                if lst[n - j - 1] != 0:
                    pos2 += 1
                else:
                    res2.append(pos2)
                    fl2 = False

            if lst[j] != 0:
                pos += 1
            else:
                res.append(pos)
                break

    res2.reverse()
    result = map(min, zip(res, res2))
    print(list(result))


zeronear(lst)









