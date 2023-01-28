"""
用环形列表实现栈和队列
"""
import random


class MyStack(object):
    stack = None
    max_size = 10

    def __init__(self, max_size=None):
        # 初始化固定大小的列表
        if max_size:
            self.max_size = max_size
        self.stack = [0] * self.max_size
        self.size = 0

    def push(self, value: int) -> None:
        if self.is_full():
            raise RuntimeError('栈满了，不能在放了！')
        index = self.size
        self.stack[index] = value
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise RuntimeError('栈空了，不能在拿了！')
        index = self.size - 1
        num = self.stack[index]
        self.size -= 1
        return num

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size


class MyQueue(object):
    queue = None
    max_size = 10

    def __init__(self, max_size=None):
        if max_size:
            self.max_size = max_size
        self.queue = [0] * max_size
        self.push_index = 0
        self.pop_index = 0
        self.size = 0

    def push(self, value: int) -> None:
        if self.is_full():
            raise RuntimeError('队列满了，不能在放了！')
        self.queue[self.push_index] = value
        self.push_index = (self.push_index + 1) % self.max_size
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise RuntimeError('队列空了，不能在拿了！')
        num = self.queue[self.pop_index]
        self.pop_index = (self.pop_index + 1) % self.max_size
        self.size -= 1
        return num

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size


def test_stack():
    stack = MyStack(4)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    while not stack.is_empty():
        num = stack.pop()
        print(num, end='->')
    print()


def test_queue():
    queue = MyQueue(5)
    for i in range(0, 100):
        num = random.randint(0, 10)
        is_push = True if random.random() < 0.5 else False
        try:
            if is_push:
                queue.push(num)
                print(f'push: {num}')
            else:
                num = queue.pop()
                print(f'pop: {num}')
        except RuntimeError as e:
            print(e)


def main():
    # test_stack()
    test_queue()


if __name__ == '__main__':
    main()
