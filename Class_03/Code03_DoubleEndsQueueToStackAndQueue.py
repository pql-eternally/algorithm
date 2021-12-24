"""
用双端队列实现栈和队列
"""
from collections import abc


class DoubleNode(object):
    value = None
    pre = None
    next = None

    def __init__(self, value):
        self.value = value


class DoubleEndQueues(object):
    """自己实现双端队列：可以从头加节点，从尾加节点，从头移除节点，从尾移除节点"""
    head = None
    tail = None

    def add_from_head(self, value: int) -> None:
        """
        从头部添加新节点
        """
        node = DoubleNode(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node

    def add_from_tail(self, value: int) -> None:
        """
        从尾部添加新节点
        """
        node = DoubleNode(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node

    def pop_from_head(self) -> int:
        """
        从头部添加新节点
        """
        if self.is_empty():
            return -1
        cur = self.head
        # 只有一个节点，清空队列
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            next_node = cur.next
            cur.next = None
            self.head = next_node
            self.head.pre = None
        return cur.value

    def pop_from_tail(self) -> int:
        """
        从尾部添加新节点
        """
        if self.is_empty():
            return -1
        cur = self.tail
        # 只有一个节点
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            pre_node = cur.pre
            cur.pre = None
            self.tail = pre_node
            self.tail.next = None
        return cur.value

    def is_empty(self) -> bool:
        """
        判断当前队列是否为空
        """
        return self.head is None

    def pop_all_from_head(self) -> abc.Generator:
        while self.head:
            value = self.pop_from_head()
            yield value

    def pop_all_from_tail(self) -> abc.Generator:
        while self.tail:
            value = self.pop_from_tail()
            yield value


class MyStack(object):
    """
    使用双端队列实现栈：后进先出
    """
    stack = None

    def __init__(self):
        self.stack = DoubleEndQueues()

    def push(self, value: int) -> None:
        self.stack.add_from_head(value)

    def pop(self) -> int:
        return self.stack.pop_from_head()

    def is_empty(self):
        return self.stack.is_empty()


class MyQueue(object):
    """
    使用双端队列实现队列：先进先出
    """
    queue = None

    def __init__(self):
        self.queue = DoubleEndQueues()

    def push(self, value: int) -> None:
        self.queue.add_from_tail(value)

    def pop(self) -> int:
        return self.queue.pop_from_head()

    def is_empty(self):
        return self.queue.is_empty()


def test_double_queues():
    double_queue = DoubleEndQueues()
    double_queue.add_from_head(1)
    double_queue.add_from_head(2)
    double_queue.add_from_head(3)
    double_queue.add_from_head(4)

    # for num in double_queue.pop_all_from_head():
    #     print(num, end='->')
    # print()
    #
    for num in double_queue.pop_all_from_tail():
        print(num, end='->')
    print()


def test_stack():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    while not stack.is_empty():
        num = stack.pop()
        print(num, end='->')
    print()


def test_queue():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    while not queue.is_empty():
        num = queue.pop()
        print(num, end='->')
    print()


def main():
    # test_double_queues()
    test_stack()
    test_queue()


if __name__ == '__main__':
    main()
