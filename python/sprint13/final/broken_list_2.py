__all__ = ('broken_search', )


def _binarySearch(array, target, left, right):
    """ Бинарный поиск элемента в массиве."""
    if right <= left:
        return -1
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    if target < array[mid]:
        return _binarySearch(array, target, left, mid)
    else:
        return _binarySearch(array, target, mid + 1, right)


def _break_search(array, left, right):
    """ Поиск индекса разрыва."""
    if right <= left:
        return right
    mid = (left + right) // 2
    if array[mid] < array[mid - 1]:
        return mid
    if array[mid] < array[left]:
        return _break_search(array, left, mid)
    elif array[mid] > array[left]:
        return _break_search(array, mid, right)


def broken_search(nums, target):
    """Поиск в сломанном массиве."""
    left = 0
    right = len(nums)
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        return -1
    if nums[0] < nums[-1]:
        return _binarySearch(nums, target, left, right)
    broken_index = _break_search(nums, left, right)
    left_part = _binarySearch(nums, target, left, broken_index)
    right_part = _binarySearch(nums, target, broken_index, right)
    if left_part == right_part == -1:
        return -1
    if left_part != -1:
        return left_part
    else:
        return right_part


if __name__ == '__main__':
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    target = 5
    res = broken_search(arr, target)
    print(res, arr.index(target))
    broken_search(arr, target)
