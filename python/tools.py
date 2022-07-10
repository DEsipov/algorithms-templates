#!-*-coding:utf-8-*-
from datetime import datetime


def timer(foo):
    def inner(*args, **kwargs):
        start_time = datetime.now()
        foo(*args, **kwargs)
        print(f'time: {datetime.now() - start_time}')

    return inner
