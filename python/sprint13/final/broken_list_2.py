# 69703435
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
        element_mid = array[mid]
        if element_mid < array[mid - 1]:
            return mid
        if array[left] < element_mid:
            return _break_search(mid, right)
        return _break_search(left, mid)

    left = 0
    right = len(array)
    if right == 1:
        if array[0] == target:
            return 0
        return -1
    if array[0] < array[-1]:
        return _binary_search(left, right)

    broken_index = _break_search(left, right)
    if target > array[broken_index]:
        left_part = _binary_search(left, broken_index)
        return left_part
    right_part = _binary_search(broken_index, right)
    return right_part



if __name__ == '__main__':
    target = 5
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    result = broken_search(arr, target)
    print(arr.index(target), result)
