

def main():
    # Получаем и парсим данные
    n = int(input())
    segments = [None] * n
    for i in range(n):
        start, end = map(int, input().split())
        segments[i] = [start, end]

    # Хак, используем встроенную сортировку питона.
    segments.sort()

    # Отсортированный список уже объединяем.
    ...

    results = []
    max_start, max_end = segments[0]
    i = 1

    while i < n:
        if max_start <= segments[i][0] <= max_end:
            _, curr_end = segments[i]
            i += 1
            if curr_end > max_end:
                max_end = curr_end
        else:
            results.append([max_start, max_end])
            max_start, max_end = segments[i]
            i += 1

    results.append([max_start, max_end])

    for res in results:
        print(*res)


if __name__ == '__main__':
    main()
