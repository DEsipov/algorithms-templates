def broken_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Сравнение
        if nums[mid] == target:
            return mid

        if ...:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    def test():
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr, 5) == 6