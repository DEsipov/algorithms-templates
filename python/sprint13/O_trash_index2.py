#!-*-coding:utf-8-*-
__author__ = 'vi'


def difference(numbers):
    result = []
    for i in range(len(numbers)-1):
        for j in range(i + 1, len(numbers)):
            result.append(abs(numbers[i] - numbers[j]))
    return result


def calc_2(lst, k):
    result = []

    def insert(result, new_item):
        if len(result) < k:
            result.append(new_item)
            return sorted(result)

        max_item = result[len(result) - 1]
        if new_item < max_item:
            result[k - 1] = new_item
            return sorted(result)
        else:
            return result

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            item = abs(lst[i] - lst[j])
            result = insert(result, item)

    return result


def calc(line, k):

    lst = []

    for x in line:
        num = ''
        while x != ' ':
            num += x

        # Получили число.


        pass

    def insert(result, new_item):
        if len(result) < k:
            result.append(new_item)
            return sorted(result)

        max_item = result[len(result) - 1]
        if new_item < max_item:
            result[k - 1] = new_item
            return sorted(result)
        else:
            return result

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            item = abs(line[i] - line[j])
            result = insert(result, item)

    return result

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


    n = int(input())
    line = input()
    k = int(input())

    # lst = list(map(int, line.split()))

    res = calc(line, k)
    print(res.pop())
