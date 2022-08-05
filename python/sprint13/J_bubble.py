#!-*-coding:utf-8-*-
__author__ = 'vi'


def sorting(lst):
    n = len(lst)
    flag = False
    for i in range(n - 1):
        done = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                done = True
                flag = True

        if not done:
            break

        print(*lst)

    if not flag:
        print(*lst)


if __name__ == '__main__':
    # n = 5
    # line = '1 1 1 1 1'
    n = int(input())
    line = input()

    lst = list(map(int, line.split()))
    sorting(lst)
