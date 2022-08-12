class User:
    def __init__(self, name, score, penalty):
        self.name = name
        self.score = score
        self.penalty = penalty

    def __gt__(self, other):
        """ Сравнение из коробки добавил, кортежное.
        :param other:
        :return:
        """
        return (self.score, self.penalty, self.name) > (
            other.score, other.penalty, other.name)

    def __repr__(self):
        return self.name

def sorting(arr, left, right):
    # Если края схлопнулись выходим.
    # FIX: тут нужен код.
    if right <= left:
        return

    # Запоминаем начальные границы.
    left_idx = left
    right_idx = right

    # Выбираем опорный элемент посередине.
    pivot_idx = (left+right) // 2
    pivot = arr[pivot_idx]

    # И пока левй указатель не дойдет не дойдет до правого.
    while left_idx <= right_idx:

        while pivot > arr[left_idx]:
            left_idx += 1

        # Двигаем правый указатель назад, пока его значение больше опорного.
        while pivot < arr[right_idx]:
            right_idx -= 1

        # Меняем местами правый и левый элемент.
        # И сдвигаем еще левый указатель вперед, правый назад.
        # Если указатели ее не схлопнулись, само собой.

        # FIXME: т.е если левый указатель меньше правого, то возвращаем массив.
        # Это неверно.
        # Если  левый указатель меньше правого,
        # То меняем местами правый и левый элемент.
        if left_idx <= right_idx:
        #     return arr
        # else:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
            right_idx -= 1
            left_idx += 1

    # FIXME:
    # Вызываем рекурсию для части от начала списка до правого указателя.
    sorting(arr, ...)
    # FIXME: Вызываем рекурсию для части от левого указателя до конца списка.
    sorting(arr, ...)

def get_results():
    """
    метод, который данные из input получает, для отправки в контекст.
    :return:
    """
    count_line = int(input())

    results = []
    for i in range(count_line):
        name, points, penalty = input().split()
        user = User(name=name, score=-int(points), penalty=int(penalty))
        results.append(user)

    return results


def get_local_results():
    """ Метод для локальной отладки.
    Ожидаемые значение при отладке локальными данными.
    # gena
    # timofey
    # alla
    # gosha
    # rita
    """
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
        # FIX - для удобства сортировки решенные задачи
        # записываем со знаком минус. Не забываем по int,
        # иначе сортировка будет работать, но не так, как ожидается.
        user = User(name=name, score=-int(points), penalty=int(penalty))
        results.append(user)
    return results

if __name__ == '__main__':
    # Для отправки в контест.
    # results = get_results()
    results = get_local_results()
    # Для отладки локальной.
    # results = get_local_results()
    sorting(results, 0, len(results) - 1)
    print(*results, sep='\n')
