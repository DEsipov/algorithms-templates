def broken_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        is_left_ord = bool(nums[left] <= nums[mid])
        is_right_ord = not is_left_ord
        left_inside = bool(nums[left] <= target < nums[mid])
        right_inside = bool(nums[mid] < target <= nums[right])

        if ((is_left_ord and left_inside)
                or (is_right_ord and not right_inside)):
            right = mid - 1
        else:
            left = mid + 1

    return -1


def get_index(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1


# if __name__ == '__main__':
#     target = 21
#     arr = [19, 20, 21, 55, 100, 101, 1, 4, 5, 6, 7, 9, 10, 12]
#     print(f'exp: {get_index(arr, target)}, real: {broken_search(arr, target)}')
#
#     line = '19 21 100 101 1 4 5 7 12'
#     arr = list(map(int, line.split()))
#     target = 5
#     print(f'exp: {get_index(arr, target)}, real: {broken_search(arr, target)}')
#
#     # assert broken_search(arr, 5) == 6
