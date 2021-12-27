"""
实现有获取栈中最小值功能的栈
使用两个栈，一个用来存数据的栈，一个用来存对应最小值的栈
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


class GetMinValueStack(object):
    # 数据栈：存放所有的数据
    data_stack = None
    # 最小值栈：存放当前数据位置中最小值，和数据栈同时push、pop
    min_value_stack = None

    def __init__(self):
        self.data_stack = MyStack()
        self.min_value_stack = MyStack()

    def push(self, value: int) -> None:
        self.data_stack.push(value)
        if self.min_value_stack.is_empty():
            min_value = value
        else:
            cur_min_value = self.min_value_stack.peek()
            min_value = min(value, cur_min_value)
        self.min_value_stack.push(min_value)

    def pop(self) -> int:
        self.min_value_stack.pop()
        return self.data_stack.pop()

    def get_min_value(self) -> int:
        if self.min_value_stack.is_empty():
            raise RuntimeError('栈空了，不能拿数了！')
        return self.min_value_stack.peek()

    def is_empty(self) -> bool:
        return self.data_stack.is_empty()


def main():
    stack = GetMinValueStack()
    stack.push(3)
    print(stack.get_min_value())
    stack.push(4)
    print(stack.get_min_value())
    stack.push(1)
    print(stack.get_min_value())
    stack.push(2)
    print(stack.get_min_value())
    stack.push(0)
    print(stack.get_min_value())

    print('pop ...')
    while not stack.is_empty():
        stack.pop()
        print(stack.get_min_value())


if __name__ == '__main__':
    main()
