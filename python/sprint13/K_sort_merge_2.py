
def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    i = j = 0
    k = lf
    while lf + i < mid and mid + j < rg:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if lf + i < mid:
        while k < rg:
            arr[k] = left[i]
            i += 1
            k += 1
    else:
        while k < rg:
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return
    else:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)

#
# if __name__ == '__main__':
#     # В входном файле лишняя строка, читаем ее, чтоб не мешалась.
#     fake_line = input()
#     n = int(input())
#     line = input()
#
#     lst = list(map(int, line.split()))
#     merge_sort(lst, 0, n)
#     print(*lst)


    # a = [1, 4, 9, 2, 10, 11]
    # b = merge(a, 0, 3, 6)
    # expected = [1, 2, 4, 9, 10, 11]
    # assert b == expected
    # c = [1, 4, 2, 10, 1, 2]
    # merge_sort(c, 0, 6)
    # expected = [1, 1, 2, 2, 4, 10]
    # assert c == expected