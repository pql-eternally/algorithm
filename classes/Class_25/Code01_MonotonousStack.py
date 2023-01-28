from typing import List, TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.data = []

    def push(self, item: T) -> None:
        self.data.append(item)

    def pop(self) -> T:
        if self.is_empty():
            return
        return self.data.pop()

    def peek(self) -> T:
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


def get_near_less_no_repeat(arr: List[int]) -> List[List[int]]:
    """
    获取左边比当前数最近最小的数的下标、右边比当前数最近最小的数的下标
    如果没有返回-1
    """
    res = [[] for _ in range(len(arr))]
    stack = Stack[int]()
    # 循环数据对比栈顶元素弹栈和压栈
    for index, num in enumerate(arr):
        while not stack.is_empty() and num < arr[stack.peek()]:
            i = stack.pop()
            # 当前i位置：左侧小的是栈顶数，右侧小顶是index位置
            res[i] = [stack.peek() or -1, index]
        stack.push(index)
    # 依次弹出栈顶元素，此时数据右侧均无比当前小的数，左侧比当前小的数在栈顶位置
    while not stack.is_empty():
        i = stack.pop()
        res[i] = [stack.peek() or -1, -1]
    return res


def get_near_less_with_repeat(arr: List[int]) -> List[List[int]]:
    """
    栈中元素存列表，当前位置和栈顶相同时，将当前位置追加到栈顶元素后面
    """
    res = [[] for _ in range(len(arr))]
    stack = Stack[List[int]]()
    # 对比压栈弹栈
    for index, num in enumerate(arr):
        while not stack.is_empty() and num < arr[stack.peek()[0]]:
            idxs = stack.pop()
            for idx in idxs:
                res[idx] = [-1 if stack.is_empty() else stack.peek()[-1], index]
        if not stack.is_empty() and arr[stack.peek()[0]] == num:
            idxs = stack.peek()
            idxs.append(index)
        else:
            stack.push([index])
    # 弹栈
    while not stack.is_empty():
        idxs = stack.pop()
        for idx in idxs:
            res[idx] = [-1 if stack.is_empty() else stack.peek()[-1], -1]
    return res


def main():
    arr = [3, 1, 5, 2, 4]
    res = get_near_less_no_repeat(arr)
    arr = [3, 1, 5, 1, 1, 2, 2, 2, 4]
    res2 = get_near_less_with_repeat(arr)
    print(res)
    print(res2)


if __name__ == '__main__':
    main()
