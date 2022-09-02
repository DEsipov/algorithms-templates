def count_less(array, desired_diff):
    count = left = 0
    for right, x in enumerate(array):
        while x - array[left] > desired_diff:
            left += 1
        count += right - left
    return count


def smallest_distance(array, k):
    array.sort()
    low = 0
    high = array[-1] - array[0]
    while low < high:
        mid = (low + high) // 2
        count = count_less(array, mid)
        if count >= k:
            high = mid
        else:
            low = mid + 1

    return low