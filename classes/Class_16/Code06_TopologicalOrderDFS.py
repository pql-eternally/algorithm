"""
给定一个有向图，图节点的拓扑排序定义如下:

对于图中的每一条有向边 A -> B , 在拓扑排序中A一定在B之前.
拓扑排序中的第一个节点可以是图中的任何一个没有其他节点指向它的节点.
针对给定的有向图找到任意一种拓扑排序的顺序.

lintcode链接：https://www.lintcode.com/problem/127/description
"""
from typing import Dict


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __str__(self):
        return f'{self.label}'


class Record:
    def __init__(self, node: DirectedGraphNode, count: int):
        self.node = node
        self.count = count

    def __lt__(self, other):
        return self.count > other.count


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def gen_record(self, node: DirectedGraphNode, node_record_map: Dict[DirectedGraphNode, Record]):
        if node in node_record_map:
            return node_record_map[node]
        count = 0
        for cur in node.neighbors:
            count += self.gen_record(cur, node_record_map).count
        record = Record(node, count + 1)
        node_record_map[node] = record
        return record

    def topSort(self, graph):
        """
        统计从每个节点出发经过的所有节点的频次，按照节点频次从大到小排序后，依次取出
        """
        node_record_map = {}
        records = []
        for node in graph:
            record = self.gen_record(node, node_record_map)
            records.append(record)
        records.sort()
        res = []
        for record in records:
            res.append(record.node)
        return res


def main():
    node0 = DirectedGraphNode(0)
    node1 = DirectedGraphNode(1)
    node2 = DirectedGraphNode(2)
    node3 = DirectedGraphNode(3)
    node4 = DirectedGraphNode(4)
    node3.neighbors = [node4]
    node2.neighbors = [node1, node4]
    node1.neighbors = [node3, node4]
    node0.neighbors = [node1, node2, node3, node4]
    graph = [node0, node1, node2, node3, node4]
    s = Solution()
    res = s.topSort(graph)
    for node in res:
        print(node)


if __name__ == '__main__':
    main()
