"""
使用两个队列来实现栈
"""
from queue import Queue

queue = Queue()


class MyStack(object):
    data_queue = None
    help_queue = None

    def __init__(self):
        self.data_queue = Queue()
        self.help_queue = Queue()

    def push(self, value: int) -> None:
        self.data_queue.put(value)

    def pop(self) -> int:
        if self.is_empty():
            raise RuntimeError('栈空了，不能拿数据了！')
        while self.data_queue.qsize() > 1:
            self.help_queue.put(self.data_queue.get())
        num = self.data_queue.get()
        # 两个队列交换，使得数据队列始终是同一个
        self.data_queue, self.help_queue = self.help_queue, self.data_queue
        return num

    def is_empty(self) -> bool:
        return self.data_queue.empty()


def main():
    # queue.put(1)
    # queue.put(2)
    # queue.put(3)
    # print(queue.get())
    # print(queue.get())
    # print(queue.get())

    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    main()
