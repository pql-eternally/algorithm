"""
使用两个栈来实现队列的功能：先进先出
"""


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

    def peek(self) -> int:
        if self.is_empty():
            raise RuntimeError('栈空了，不能在拿了！')
        index = self.size - 1
        return self.stack[index]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.max_size


class MyQueue(object):
    max_size = 10
    push_stack = None
    pop_stack = None

    def __init__(self):
        self.push_stack = MyStack(self.max_size)
        self.pop_stack = MyStack(self.max_size)

    def push(self, value: int) -> None:
        self.push_stack.push(value)

    def pop(self) -> int:
        if self.is_empty():
            raise RuntimeError('队列空了，不能在拿了！')
        if self.pop_stack.is_empty():
            self._push_to_pop()
        return self.pop_stack.pop()

    def _push_to_pop(self) -> None:
        """
        将push栈里面所有的数据放入pop栈中
        """
        while not self.push_stack.is_empty():
            self.pop_stack.push(self.push_stack.pop())

    def is_empty(self) -> bool:
        return self.push_stack.is_empty() and self.pop_stack.is_empty()


def main():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    queue.push(4)
    print(queue.pop())
    queue.push(5)
    print(queue.pop())


if __name__ == '__main__':
    main()
