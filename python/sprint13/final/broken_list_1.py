from typing import List


def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
    '''Стандартный бинарный поиск элемента.'''
    if right <= left:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search(nums, target, left, mid)
    elif target > nums[mid]:
        return binary_search(nums, target, mid + 1, right)


def binary_search_broken(nums: List[int], left: int, right: int) -> int:
    '''Бинарный поиск индекса элемента, с которого ломается последовательность.'''

    if right <= left:
        return right
    mid = (left + right) // 2

    if nums[mid] < nums[mid - 1]:
        return mid
    elif nums[mid] < nums[left]:
        return binary_search_broken(nums, left, mid)
    elif nums[mid] > nums[left]:

        # Вернул твои старые условия.
        return binary_search_broken(nums, mid + 1, right)  # Вот здесь раньше было

        # return binary_search_broken(nums, mid, right)  # Вот здесь раньше было
        # так: binary_search_broken(nums, mid + 1, right), т.к. мне ошибочно
        # казалось, что эта единица поможет выбраться из замкнутого цикла

    # Вот здесь функция, если не выполнится ни одно из условий, ничего не
    # вернет, т.е. вернет None
    # Например, если nums[mid] == nums[left]
    print(nums[mid], nums[left])
    print('a')


def broken_search(nums: List[int], target: int) -> int:
    '''Ищем индекс требуемого элемента.'''
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    broken = False
    if nums[0] > nums[-1]:
        broken = True
        broken_index = binary_search_broken(nums, 0, len(nums))

    if broken:  # Если последовательность сломана, делим на два подмассива, и
        # используем бинарный поиск для каждого подмассива
        result_nums_min = binary_search(
            nums, target, broken_index, len(nums)
        )
        if result_nums_min == -1:
            result_nums_max = binary_search(nums, target, 0, broken_index)
            return result_nums_max
        else:
            return result_nums_min
    else:  # Если последовательность не сломана, используем бинарный поиск
        return binary_search(nums, target, 0, len(nums))


if __name__ == '__main__':
    arr = [555, 558, 559, 560, 561, 564, 567, 570, 571, 572, 580, 581, 582,
           583, 585, 586, 587, 588, 590, 591, 592, 594, 595, 597, 599, 600,
           605, 607, 610, 612, 613, 614, 616, 619, 620, 621, 624, 626, 627,
           628, 629, 631, 632, 633, 636, 637, 640, 641, 642, 643, 644, 645,
           648, 649, 650, 651, 652, 653, 655, 656, 660, 662, 663, 665, 666,
           667, 668, 669, 673, 674, 676, 677, 679, 683, 684, 685, 686, 687,
           688, 689, 691, 692, 698, 700, 702, 707, 709, 711, 714, 715, 717,
           719, 722, 725, 728, 730, 731, 733, 734, 737, 738, 739, 740, 741,
           746, 747, 748, 749, 750, 751, 752, 755, 756, 760, 761, 765, 766,
           767, 769, 770, 771, 772, 773, 775, 778, 779, 780, 783, 785, 789,
           793, 795, 796, 797, 799, 801, 803, 804, 806, 807, 810, 811, 812,
           813, 814, 815, 817, 819, 823, 824, 830, 833, 835, 836, 838, 839,
           840, 841, 842, 845, 846, 848, 852, 853, 856, 857, 858, 859, 864,
           866, 873, 875, 876, 877, 878, 879, 880, 881, 884, 887, 889, 891,
           893, 897, 904, 906, 907, 909, 911, 912, 914, 915, 916, 918, 919,
           920, 924, 926, 930, 931, 932, 934, 935, 936, 939, 941, 942, 944,
           946, 948, 949, 951, 952, 953, 954, 958, 959, 960, 961, 962, 963,
           965, 966, 967, 968, 971, 972, 977, 978, 979, 980, 984, 988, 989,
           992, 995, 999, 1000, 1, 2, 4, 5, 7, 11, 14, 18, 20, 21, 23, 25, 27,
           29, 30, 36, 39, 47, 48, 50, 53, 54, 56]

    print(binary_search_broken(arr, 0, len(arr)))
