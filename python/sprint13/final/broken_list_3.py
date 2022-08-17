
# контест ожидает функцию broken_search, а не main_search, переименуй.
def broken_search(array, target):
    def _binary_search(left, right):
        """ Бинарный поиск элемента в массиве."""
        if right <= left:
            return -1
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if target < array[mid]:
            return _binary_search(left, mid)
        else:
            return _binary_search(mid + 1, right)

    def _break_search(left, right):
        """ Поиск индекса разрыва."""
        if right <= left:
            return right
        mid = (left + right) // 2
        if array[mid] < array[mid - 1]:
            return mid
        if array[mid] < array[left]:
            return _break_search(left, mid)
        if array[mid] > array[left]:
            return _break_search(mid, right)
        return _break_search(left, mid)

    def broken_search():
        """Поиск в сломанном массиве."""
        left = 0
        right = len(array)
        if len(array) == 1:
            if array[0] == target:
                return 0
            return -1
        if array[0] < array[-1]:
            return _binary_search(left, right)
        broken_index = _break_search(left, right)
        left_part = _binary_search(left, broken_index)
        right_part = _binary_search(broken_index, right)
        if left_part == right_part == -1:
            return -1
        if left_part != -1:
            return left_part
        else:
            return right_part

    return broken_search()
