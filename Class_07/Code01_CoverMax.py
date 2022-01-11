"""
给定很多线段，每个线段都有两个数[start, end]，
表示线段开始位置和结束位置，左右都是闭区间
规定：
1）线段的开始和结束位置一定都是整数值
2）线段重合区域的长度必须>=1
返回线段最多重合区域中，包含了几条线段
"""
import random
from queue import PriorityQueue


class MyPriorityQueue(PriorityQueue):

    def peek(self):
        if not self.empty():
            return self.queue[0]


class Line(object):

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self):
        return f'[{self.start}, {self.end}]'


def sort_by_start_asc(line):
    return line.start


def sort_by_start_desc(line):
    return -line.start


def sort_by_end_asc(line):
    return line.end


def max_cover(lines: list) -> int:
    # 按线段起点位置从小到大排序
    lines.sort(key=sort_by_start_asc)
    # 优先级队列，小根堆
    heap = MyPriorityQueue()
    cover = 0
    for line in lines:
        # 弹出堆中线段终点位置小于当前线起点，求出当前线段重合区域的长度
        while not heap.empty() and heap.peek() <= line.start:
            heap.get()
        heap.put(line.end)
        cover = max(cover, heap.qsize())
    return cover


def comparator(lines: list) -> int:
    """
    暴力法
    """
    min_value = None
    max_value = None
    for line in lines:
        if min_value is None:
            min_value = line.start
            max_value = line.end
        else:
            min_value = min(min_value, line.start)
            max_value = max(max_value, line.end)
    cover = 0
    for value in range(min_value, max_value):
        point = value + 0.5
        cur_cover = 0
        for line in lines:
            if line.start < point < line.end:
                cur_cover += 1
        cover = max(cover, cur_cover)
    return cover


def random_lines(max_size=5) -> list:
    lines = []
    for i in range(random.randint(1, max_size)):
        p1 = random.randint(0, 99)
        p2 = random.randint(p1 + 1, 100)
        line = Line(p1, p2)
        lines.append(line)
    return lines


def print_lines(lines: list) -> None:
    for line in lines:
        print(line, end=',')
    print()


def main() -> None:
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        lines = random_lines()
        # print_lines(lines)
        # lines.sort(key=sort_by_start_desc)
        # print_lines(lines)
        # lines.sort(key=sort_by_end_asc)
        # print_lines(lines)
        res1 = max_cover(lines)
        res2 = comparator(lines)
        if res1 != res2:
            print(print_lines(lines), res1, res2)
            break
    print('Done ...')


if __name__ == '__main__':
    main()
