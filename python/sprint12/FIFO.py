#!-*-coding:utf-8-*-


class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            old_tail = self.tail
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

            print(f'push: {x}, size: {self.size}, '
                  f'tail_old: {old_tail}, tail_new: {self.tail}')


def test_queue():
    queue = Queue(4)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)


if __name__ == '__main__':
    test_queue()
