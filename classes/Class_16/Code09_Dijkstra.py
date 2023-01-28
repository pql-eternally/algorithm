"""
单元最短路径算法Dijkstra（迪杰斯特拉算法）
迪科斯彻算法使用了广度优先搜索解决赋权有向图或者无向图的单源最短路径问题，算法最终得到一个最短路径树
"""

from typing import List, Dict, Set
from heapq import heapify, heappush, heappop
from graph import Node, Edge, Graph, GraphGenerator


def choose_node(distance_map: Dict, selected_nodes: Set):
    """
    当前未被选择距离最近的点
    """
    min_node = None
    min_distance = 99999
    for node, distance in distance_map.items():
        if node not in selected_nodes and distance < min_distance:
            min_distance = distance
            min_node = node
    return min_node


def dijkstra_short_path(start: Node):
    """
    从开始节点求出到图中所有节点的最短路径表
    """
    # 距离表
    distance_map = {
        start: 0
    }
    # 已经锁定的节点
    selected_nodes = set()
    min_node = choose_node(distance_map, selected_nodes)
    while min_node:
        distance = distance_map.get(min_node)
        for edge in min_node.edges:
            from_node = edge.from_node
            to_node = edge.to_node
            if from_node != min_node and from_node not in selected_nodes:
                node = from_node
            elif to_node != min_node and to_node not in selected_nodes:
                node = to_node
            else:
                continue
            if node not in distance_map:
                distance_map[node] = distance + edge.weight
            else:
                distance_map[node] = min(distance_map[node], distance + edge.weight)
        selected_nodes.add(min_node)
        min_node = choose_node(distance_map, selected_nodes)
    return distance_map


def main():
    matrix = [
        [1, 1, 6],
        [6, 1, 2],
        [5, 1, 5],
        [3, 2, 3],
        [5, 2, 6],
        [5, 5, 6],
        [6, 3, 4],
        [6, 3, 6],
        [4, 4, 6],
        [2, 4, 5]
    ]
    graph = GraphGenerator.create_undigraph(matrix)
    distance_map = dijkstra_short_path(graph.nodes[1])
    for node, distance in distance_map.items():
        print(node, distance)


if __name__ == '__main__':
    main()
