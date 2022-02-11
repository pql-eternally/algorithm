"""
给定一个栈，请逆序这个栈，不能申请额外的数据结构，只能使用递归函数
"""


class MyStack(object):
    stack = None
    max_size = 10

    def __init__(self, max_size=None):
        if max_size:
            self.max_size = max_size
        self.stack = []
        self.size = 0

    def push(self, value: int) -> None:
        if self.is_full():
            raise RuntimeError('栈满了，不能在放了！')
        self.stack.append(value)
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise RuntimeError('栈空了，不能在拿了！')
        self.size -= 1
        return self.stack.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise RuntimeError('栈空了，不能在拿了！')
        index = self.size - 1
        return self.stack[index]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.max_size

    def __str__(self):
        return ','.join(map(str, self.stack))


def pop_stack_bottom(stack: MyStack):
    """
    弹出栈底元素并返回
    """
    result = stack.pop()
    if stack.is_empty():
        return result
    value = pop_stack_bottom(stack)
    stack.push(result)
    return value


def reverse_stack(stack: MyStack):
    if stack.is_empty():
        return
    value = pop_stack_bottom(stack)
    reverse_stack(stack)
    stack.push(value)


def main():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    reverse_stack(stack)
    print(stack)


if __name__ == '__main__':
    main()
