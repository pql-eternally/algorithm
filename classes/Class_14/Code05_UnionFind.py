"""
并查集的实现
并查集，在一些有N个元素的集合应用问题中，我们通常是在开始时让每个元素构成一个单元素的集合，然后按一定顺序将属于同一组的元素所在的集合合并，其间要反复查找一个元素在哪个集合中

主要操作
初始化
    把每个点所在集合初始化为其自身。
    通常来说，这个步骤在每次使用该数据结构时只需要执行一次，无论何种实现方式，时间复杂度均为O(N)
查找
    查找元素所在的集合，即根节点。
合并
    将两个元素所在的集合合并为一个集合。
    通常来说，合并之前，应先判断两个元素是否属于同一集合，这可用上面的“查找”操作实现。
"""


class Node(object):
    value: str

    def __init__(self, v):
        self.value = v

    def __str__(self):
        return self.value


class UnionFind(object):
    nodes: dict = None
    parents: dict = None
    sizes: dict = None

    def __init__(self, values: list):
        self.nodes = {}
        self.parents = {}
        self.sizes = {}
        for v in values:
            node = Node(v)
            self.nodes[v] = node
            self.parents[node] = node
            self.sizes[node] = 1

    def find(self, cur: Node) -> Node:
        path = []
        while cur != self.parents.get(cur):
            path.append(cur)
            cur = self.parents[cur]
        # 扁平化
        while path:
            self.parents[path.pop()] = cur
        return cur

    def union(self, a: str, b: str):
        node_a = self.nodes.get(a)
        node_b = self.nodes.get(b)
        a_head = self.find(node_a)
        b_head = self.find(node_b)
        if a_head != b_head:
            a_size = self.sizes[node_a]
            b_size = self.sizes[node_b]
            if a_size > b_size:
                small, big = b_head, a_head
            else:
                small, big = a_head, b_head
            self.parents[small] = big
            self.sizes[big] = a_size + b_size
            self.sizes.pop(small)

    def is_same_set(self, a: str, b: str):
        return self.find(self.nodes.get(a)) == self.find(self.nodes.get(b))

    def sets(self) -> int:
        return len(self.sizes)


def main():
    union_find = UnionFind(['a', 'b', 'c', 'd', 'e'])
    union_find.union('a', 'b')
    print(union_find.sets())
    print(union_find.parents)


if __name__ == '__main__':
    main()
