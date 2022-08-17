class User:
    def __init__(self, name, score, penalty):
        self.name = name
        self.score = score
        self.penalty = penalty

    def __gt__(self, other):
        return (self.score, self.penalty, self.name) > (
            other.score, other.penalty, other.name)

    def __repr__(self):
        return self.name




# Внешняя, которую вызовешь в main.
def sorting(results, start, end):

    # Внутренняя.Объявление.
    def sorting_inner(left, right):
        # Причем внутри можно эта функция будет видеть
        # переменные внешней функции. Например.
        results.append()

    # Вызов внутренней функции.
    sorting_inner(start, end)




def sorting(results, start, end):
    if end - start == 0:
        return
    elif end - start == 1:
        if results[start] < results[end]:
            results[start], results[end] = results[end], results[start]
        return

    left, right = 0, 0
    if right <= left:
        return

    mid_result = results[start + (end - start) // 2]
    while left + right < end - start:
        left_result = results[start + left]
        right_result = results[end - right]
        if mid_result < left_result:
            left += 1
        elif mid_result > right_result:
            right += 1
        else:
            results[start + left] = right_result
            results[end - right] = left_result
    sorting(results, start, start + left)
    sorting(results, start + left + 1, end)


def get_inputs():
    results = [input().split() for _ in range(int(input()))]
    for i in range(len(results)):
        results[i] = User(results[i][0], int(results[i][1]), int(results[i][2]))
    return results


def get_local_results():
    lines = (
        'alla 4 100',
        'gena 6 1000',
        'gosha 2 90',
        'rita 2 90',
        'timofey 4 80',
    )

    results = []
    for line in lines:
        name, points, penalty = line.split()
        user = User(name=name, score=-int(points), penalty=int(penalty))
        results.append(user)

    return results


def get_results():
    count_line = int(input())
    results = []

    for i in range(count_line):
        name, points, penalty = input().split()
        user = User(name=name, score=-int(points), penalty=int(penalty))
        results.append(user)

    return results


if __name__ == '__main__':
    # results = get_local_results()
    results = get_results()
    sorting(results, 0, len(results) - 1)
    print(*results, sep='\n')


# expected
# gena
# timofey
# alla
# gosha
# rita
