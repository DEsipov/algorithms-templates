from typing import List, Tuple

"""
Вам дана статистика по числу запросов в секунду к вашему любимому 
рекомендательному сервису. 
Измерения велись n секунд. 
В секунду i поступает qi запросов. 
Примените метод скользящего среднего с длиной окна k к этим данным 
и выведите результат.
"""


def moving_average(timeseries, k):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:k])
    result.append(current_sum / k)
    for i in range(0, len(timeseries) - k):
        current_sum -= timeseries[i]
        current_sum += timeseries[i + k]
        current_avg = current_sum / k
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
