#!-*-coding:utf-8-*-
__author__ = 'vi'


LEFT = 0
RIGTH = 1
MERGE = 2


def compare_join(l_segment, r_segment):
    # Сравниваем по старту.
    change = False
    if l_segment[0] < r_segment[0]:
        left, right = l_segment, r_segment
    else:
        change = True
        right, left = l_segment, r_segment

    # Объединение.
    if left[1] >= right[0]:
        end = left[1] if left[1] > right[1] else right[1]
        # print('item', left[0], end)
        return (left[0], end), MERGE

    # Не пересекаются.
    # print('item', left)
    return left, RIGTH if change else LEFT


def sorting2(segments):
    length = len(segments)

    if length == 1:
        return segments
    else:
        mid = length // 2 + length % 2

        l_segments = sorting2(segments[:mid])
        r_segments = sorting2(segments[mid:])

        l, r = 0, 0
        res = []
        while l < len(l_segments) and r < len(r_segments):
            item, mode = compare_join(l_segments[l], r_segments[r])
            res.append(item)
            if mode == LEFT:
                l += 1
            elif mode == RIGTH:
                r += 1
            else:
                l += 1
                r += 1

        while l < len(l_segments):
            res.append(l_segments[l])
            l += 1

        while r < len(r_segments):
            res.append(r_segments[r])
            r += 1

        # print(f'res: {res}')

        return res


def local_get_n():
    return 6


def get_n():
    return int(input())


def parse_lines(lines):
    res = []
    for line in lines:
        start, end = line.split()
        res.append((int(start), int(end)))
    return res


def local_get_segments():
    # lines = [
    #     '7 8',
    #     '7 8',
    #     '2 3',
    #     '6 10',
    # ]

    # lines = [
    #     '2 3',
    #     '5 6',
    #     '3 4',
    #     '3 4',
    # ]

    lines = [
        '1 3',
        '3 5',
        '4 6',
        '5 6',
        '2 4',
        '7 10',
    ]

    return parse_lines(lines)


def get_segments(n):
    segments = [[int(i) for i in input().split()] for _ in range(n)]
    return segments


if __name__ == '__main__':
    n = local_get_n()
    # n = get_n()

    segments = local_get_segments()

    # res = []
    # for item in segments:
    #     pass
    # segments = get_segments(n)

    result = sorting2(segments)
    # expected = ('2 3', '6 10')
    expected = ('1 6', '7 10')
    # print(f'segments: {segments}')
    # print(f'expected: {expected}')
    # print(f'result: {result}')
    for line in result:
        print(f'{line[0]} {line[1]}')
