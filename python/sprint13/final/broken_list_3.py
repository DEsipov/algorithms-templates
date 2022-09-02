import sys
import threading

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)


def binarySearch(nums, target, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binarySearch(nums, target, left, mid)
    else:
        return binarySearch(nums, target, mid + 1, right)


def broken_search(nums, target, left=0, right=None) -> int:
    if right is None:
        right = len(nums)

    if right <= left:
        break_value = len(nums) - 1
    elif len(nums) == 1:
        break_value = 0
    else:
        mid = (left + right) // 2
        if nums[mid] < nums[mid - 1]:
            break_value = mid
        elif nums[mid] > nums[mid + 1]:
            break_value = mid + 1
        elif mid != 0:
            return broken_search(nums, target, left, mid)
        else:
            mid = len(nums) // 2
            right = len(nums)
            return broken_search(nums, target, mid + 1, right)

    if break_value == 0:
        return binarySearch(nums, target, 0, len(nums))
    else:
        if nums[break_value] <= target <= nums[-1]:
            return binarySearch(nums, target, break_value, len(nums))
        else:
            return binarySearch(nums, target, 0, break_value)


if __name__ == '__main__':
    target = 5
    expected = 6
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    broken_search(arr, target)
    print(arr.index(target), expected)
