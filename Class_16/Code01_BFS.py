"""
实现图的宽度优先遍历
"""
from graph import Node, Edge, Graph, GraphGenerator


def bfs(start: Node):
    """
    从开始节点进行宽度优先遍历
    """
    if not start:
        return

    queue = []
    nodes = set()
    queue.append(start)
    nodes.add(start)
    while queue:
        cur = queue.pop(0)
        print(cur.value)
        for node in cur.neighbors:
            if node not in nodes:
                queue.append(node)
                nodes.add(node)


if __name__ == '__main__':
    matrix = [
        [3, 1, 2],
        [1, 1, 6],
        [4, 1, 3],
        [1, 2, 4],
        [2, 2, 5],
        [3, 6, 3],
        [3, 6, 7],
        [5, 7, 8],
        [4, 8, 3],
    ]
    graph = GraphGenerator.create(matrix)
    start = graph.nodes[1]
    bfs(start)
