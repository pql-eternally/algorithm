"""
做一个加强堆的题目，给定一个整型数组，int[] arr；和一个布尔类型数组，boolean[] op
两个数组一定等长，假设长度为N，arr[i]表示客户编号，op[i]表示客户操作
arr= [3,3,1,2,1,2,5…
op = [T,T,T,T,F,T,F…
依次表示：
3用户购买了一件商品
3用户购买了一件商品
1用户购买了一件商品
2用户购买了一件商品
1用户退货了一件商品
2用户购买了一件商品
5用户退货了一件商品…
一对arr[i]和op[i]就代表一个事件：
用户号为arr[i]，op[i] == T就代表这个用户购买了一件商品，op[i] == F就代表这个用户退货了一件商品
现在你作为电商平台负责人，你想在每一个事件到来的时候，
都给购买次数最多的前K名用户颁奖。
所以每个事件发生后，你都需要一个得奖名单（得奖区）。
得奖系统的规则：
1，如果某个用户购买商品数为0，但是又发生了退货事件，则认为该事件无效，得奖名单和上一个事件发生后一致，例子中的5用户
2，某用户发生购买商品事件，购买商品数+1，发生退货事件，购买商品数-1
3，每次都是最多K个用户得奖，K也为传入的参数，如果根据全部规则，得奖人数确实不够K个，那就以不够的情况输出结果
4，得奖系统分为得奖区和候选区，任何用户只要购买数>0，一定在这两个区域中的一个
5，购买数最大的前K名用户进入得奖区，在最初时如果得奖区没有到达K个用户，那么新来的用户直接进入得奖区
6，如果购买数不足以进入得奖区的用户，进入候选区
7，如果候选区购买数最多的用户，已经足以进入得奖区，
     该用户就会替换得奖区中购买数最少的用户（大于才能替换），
     如果得奖区中购买数最少的用户有多个，就替换最早进入得奖区的用户
     如果候选区中购买数最多的用户有多个，机会会给最早进入候选区的用户
8，候选区和得奖区是两套时间，
     因用户只会在其中一个区域，所以只会有一个区域的时间，另一个没有
     从得奖区出来进入候选区的用户，得奖区时间删除，
     进入候选区的时间就是当前事件的时间（可以理解为arr[i]和op[i]中的i）
     从候选区出来进入得奖区的用户，候选区时间删除，
     进入得奖区的时间就是当前事件的时间（可以理解为arr[i]和op[i]中的i）
9，如果某用户购买数==0，不管在哪个区域都离开，区域时间删除，
     离开是指彻底离开，哪个区域也不会找到该用户
     如果下次该用户又发生购买行为，产生>0的购买数，
     会再次根据之前规则回到某个区域中，进入区域的时间重记
请遍历arr数组和op数组，遍历每一步输出一个得奖名单
public List<List<Integer>>  topK (int[] arr, boolean[] op, int k)

步骤：
1、得奖区、候选区，都是堆，
    得奖区为小顶堆（先比较购买数量小的在堆顶，如果购买数量相同进入得奖区时间早的在堆顶）
    候选区为大顶堆（先比较购买数量大的在堆顶，如果购买数量相同进入候选区时间早的在堆顶）
2、每次发生操作更新当前id所在的区域
3、比较两个区域堆顶元素是否达到了交换的条件
"""
# TODO：业务逻辑复杂，后面再完善


class Customer(object):
    id: int
    buy: int = 0
    enter_time: int = 0

    def __init__(self, _id: int, buy: int, time: int):
        self.id = _id
        self.buy = buy
        self.enter_time = time

    def __str__(self):
        return f'id: {self.id}, buy: {self.buy}, enter_time: {self.enter_time}'


class Comparator(object):

    def compare(self, c1: Customer, c2: Customer):
        return 1


class HeapCreator(object):
    heap: list = None
    # 索引表
    index_map: dict = None
    heap_size: int = 0
    comp: object = None

    def __init__(self, c: Comparator):
        self.heap = []
        self.heap_size = 0
        self.index_map = {}
        self.comp = c()

    def heapify(self, index) -> int:
        """
        从index位置，往下看，不断的下沉
        停：较小的孩子都不再比index位置的数小；已经没孩子了
        返回新的index值
        """
        child_index = (index << 1) + 1
        while child_index < self.heap_size:
            right_child_index = child_index + 1
            if right_child_index < self.heap_size and self.comp.compare(self.heap[right_child_index],
                                                                        self.heap[child_index]) < 0:
                child_index = right_child_index
            if self.comp.compare(self.heap[index], self.heap[child_index]) < 0:
                break
            self.swap(index, child_index)
            index = child_index
            child_index = (index << 1) + 1
        return index

    def heap_insert(self, index) -> int:
        """
        新加进来的数，现在停在了index位置，请依次往上移动，
        移动到0位置，或者干不掉自己的父亲了，停！
        返回新的index值
        """
        parent_index = (index - 1) >> 1
        while parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) >> 1
        return index

    def is_empty(self):
        return self.heap_size == 0

    def size(self):
        return self.heap_size

    def contains(self, value: Customer) -> bool:
        """
        查看当前值是否存在堆中
        """
        return value in self.index_map

    def push(self, value: Customer) -> None:
        """
        堆中添加元素
        """
        self.heap.append(value)
        self.heap_size += 1
        index = self.heap_size - 1
        index = self.heap_insert(index)
        self.index_map[value] = index

    def pop(self) -> Customer:
        """
        移除堆顶元素
        """
        if self.is_empty():
            raise RuntimeError('empty')
        last_index = self.heap_size - 1
        self.swap(0, last_index)
        item = self.heap.pop(last_index)
        self.heap_size -= 1
        self.index_map.pop(item)
        self.heapify(0)
        return item

    def remove(self, value: Customer):
        """
        移除堆中当前值，并保证堆有序
        """
        if value not in self.index_map:
            raise RuntimeError('Not exist')
        index = self.index_map[value]
        last_index = self.heap_size - 1
        if index != last_index:
            self.swap(index, last_index)
        self.heap.pop(last_index)
        self.heap_size -= 1
        self.index_map.pop(value)
        self.resign(index)

    def resign(self, index: int):
        """
        调整堆
        """
        self.heapify(index)
        self.heap_insert(index)

    def peek(self):
        """
        查看堆顶元素，不进行移除
        """
        if self.is_empty():
            raise RuntimeError('empty')
        return self.heap[0]

    def get_all_elements(self):
        """
        获取堆中所有元素
        """
        return self.heap

    def swap(self, i: int, j: int) -> None:
        """
        交换堆中两个位置元素
        """
        heap = self.heap
        self.index_map[heap[i]] = j
        self.index_map[heap[j]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def __str__(self):
        return ', '.join(map(str, self.get_all_elements()))


class CustomerMinHeap(Customer, HeapCreator):

    def __lt__(self, other):
        if self.buy != other.buy:
            return self.buy < other.buy
        return self.enter_time < other.enter_time


class CustomerMaxHeap(Customer, HeapCreator):

    def __lt__(self, other):
        if self.buy != other.buy:
            return self.buy > other.buy
        return self.enter_time < other.enter_time


def top_k(arr: list, op: list, k: int):
    pass


def print_customers(customers: list) -> None:
    for customer in customers:
        print(customer)
    print('=' * 20)


def main():
    c1 = Customer(1, 2, 2)
    c2 = Customer(2, 3, 5)
    c3 = Customer(3, 1, 4)
    c4 = Customer(4, 2, 3)
    customers = [c1, c2, c3, c4]
    print_customers(customers)
    customers.sort()
    print_customers(customers)


if __name__ == '__main__':
    main()
