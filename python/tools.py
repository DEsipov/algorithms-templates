#!-*-coding:utf-8-*-
from datetime import datetime


def timer(foo):
    def inner(*args, **kwargs):
        start_time = datetime.now()
        foo(*args, **kwargs)
        print(f'time: {datetime.now() - start_time}')

    return inner


# Кол-во тактов за одну операцию.
TAKT_NUM = 10
# Кол-во тактов в секунду 2.5 ГГц
TAKT_TIME = 2.5 * 10 ** 9


def benchmark(operations):
    takts = operations * TAKT_NUM
    time = takts / TAKT_TIME
    return time
