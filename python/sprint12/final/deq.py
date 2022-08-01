#!-*-coding:utf-8-*-

ERROR_MESSAGE = 'error'


class UnknowCommandError(Exception):
    pass


class DeqError(Exception):
    pass


class Deq:

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.max_n

    def execute(self, command_line):
        lst = command_line.split()
        command_name = lst[0]

        if command_name == 'push_back':
            item = lst[1]
            self.push_back(item)
        elif command_name == 'pop_back':
            return self.pop_back()
        elif command_name == 'pop_front':
            return self.pop_front()
        elif command_name == 'push_front':
            item = lst[1]
            self.push_front(item)
        else:
            raise UnknowCommandError()

    def push_back(self, x):
        if self.is_full():
            raise DeqError()

        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise DeqError()

        x = self.queue[self.tail - 1]
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1

        return x

    def push_front(self, x):
        if self.is_full():
            raise DeqError()

        self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = x
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise DeqError()

        x = self.queue[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1

        return x


def local_get_size(command_count=3, deque_size=3):
    return command_count, deque_size


def local_run_commands(deq: Deq):
    commands = (
        'push_front 1',
        'push_back 2',
        'push_front 2',
        'push_back 4',
        'push_back 3',
        'pop_front',
        'pop_front',
        'pop_front',
        'pop_front',
        'pop_back',
        'pop_back',
        'pop_back',
        'push_back 4',
        'pop_back',
        'push_front 777',
        'pop_front',
        'pop_front',
    )
    for command in commands:
        try:
            print(command)
            item = deq.execute(command)
            if item:
                print(item)
        except DeqError:
            print(ERROR_MESSAGE)


def get_size():
    command_count = int(input())
    deque_size = int(input())
    return command_count, deque_size


def run_commands(command_count, deq):
    for _ in range(command_count):
        command = input()
        try:
            value = deq.execute(command)
            if value:
                print(value)
        except DeqError:
            print(ERROR_MESSAGE)


if __name__ == '__main__':
    # command_count, deque_size = local_get_size()
    command_count, deque_size = get_size()
    deq = Deq(deque_size)
    # local_run_commands(deq)
    run_commands(command_count, deq)
