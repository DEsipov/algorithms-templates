import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


def binarySearch(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


def broken_search(nums, target, left=0, right=1) -> int:
    if right == len(nums):
        break_value = -1
    else:
        if nums[right] < nums[left]:
            break_value = left
        else:
            return broken_search(nums, target, left+1, right+1)
    if break_value == -1:
        return binarySearch(nums, target, 0, len(nums))
    else:
        if nums[break_value+1] <= target <= nums[-1]:
            return binarySearch(nums, target, break_value+1, len(nums))
        else:
            return binarySearch(nums, target, 0, break_value+1)


if __name__ == '__main__':
    target = 5
    expected = 6
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    print(arr.index(target), expected)
