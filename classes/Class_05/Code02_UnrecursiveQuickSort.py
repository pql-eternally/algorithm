"""
快排非递归版
"""
import copy
import random


class Op(object):
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


class MyStack(object):
    stack = None
    max_size = 10

    def __init__(self, max_size=None):
        # 初始化固定大小的列表
        if max_size:
            self.max_size = max_size
        self.stack = []
        self.size = 0

    def push(self, value: Op) -> None:
        if self.is_full():
            raise RuntimeError('栈满了，不能在放了！')
        self.stack.append(value)
        self.size += 1

    def pop(self) -> Op:
        if self.is_empty():
            raise RuntimeError('栈空了，不能在拿了！')
        self.size -= 1
        return self.stack.pop()

    def peek(self) -> Op:
        if self.is_empty():
            raise RuntimeError('栈空了，不能在拿了！')
        index = self.size - 1
        return self.stack[index]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.max_size


def quick_sort(arr: list) -> None:
    """
    快速排序
    """
    # process_recursive(arr, 0, len(arr) - 1)
    process_non_recursive(arr, 0, len(arr) - 1)


def process_non_recursive(arr: list, left: int, right: int) -> None:
    """
    使用递归实现，相当于借用系统栈
    非递归实现，要自己使用栈来实现
    """
    r = random.randint(left, right)
    arr[r], arr[right] = arr[right], arr[r]
    p1, p2 = nether_lands_flag(arr, left, right)
    stack = MyStack(max_size=1000)
    op1 = Op(left, p1 - 1)
    op2 = Op(p2 + 1, right)
    stack.push(op1)
    stack.push(op2)
    while not stack.is_empty():
        op = stack.pop()
        if op.left < op.right:
            r = random.randint(op.left, op.right)
            arr[r], arr[op.right] = arr[op.right], arr[r]
            p1, p2 = nether_lands_flag(arr, op.left, op.right)
            stack.push(Op(op.left, p1 - 1))
            stack.push(Op(p2 + 1, op.right))


def process_recursive(arr: list, left: int, right: int) -> None:
    """
    递归版
    """
    if left >= right:
        return
    r = random.randint(left, right)
    arr[r], arr[right] = arr[right], arr[r]
    p1, p2 = nether_lands_flag(arr, left, right)
    process_recursive(arr, left, p1 - 1)
    process_recursive(arr, p2 + 1, right)


def nether_lands_flag(arr: list, left: int, right: int) -> tuple:
    """
    荷兰国旗问题
    """
    if right < left:
        return -1, -1
    if left == right:
        return left, right
    p1 = left - 1
    p2 = right
    # 目标数
    target_num = arr[right]
    index = left
    while index < p2:
        cur_num = arr[index]
        if cur_num < target_num:
            p1 += 1
            arr[index], arr[p1] = arr[p1], arr[index]
            index += 1
        elif cur_num == target_num:
            index += 1
        else:
            p2 -= 1
            arr[index], arr[p2] = arr[p2], arr[index]
    # 目标数和大于区域第一个数进行交换
    arr[right], arr[p2] = arr[p2], arr[right]
    return p1 + 1, p2


def generate_random_arr(max_size: int = 20, min_value: int = 0, max_value: int = 100) -> list:
    """
    生成随机数组
    """
    size = random.randint(1, max_size)
    arr = []
    for i in range(0, size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    return arr


def comparator(arr: list) -> None:
    arr.sort()


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(100)
        arr1 = copy.copy(arr)
        arr2 = copy.copy(arr)
        quick_sort(arr1)
        comparator(arr2)
        if arr1 != arr2:
            print(f'arr: {arr}，res1：{arr1}，res2：{arr2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
