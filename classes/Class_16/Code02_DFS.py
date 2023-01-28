"""
实现图的深度优先遍历
"""
from graph import Node, Edge, Graph, GraphGenerator, List


def dfs(start: Node, nodes: List = None):
    """
    图深度优先遍历，从一条边一直遍历下去，直到走完
    递归方式
    """
    if not start:
        return
    if not nodes:
        nodes = []
    print(start.value)
    nodes.append(start)
    for node in start.neighbors:
        if node not in nodes:
            dfs(node, nodes)


def dfs2(start: Node):
    """
    图深度优先遍历，从一条边一直遍历下去，直到走完
    使用栈
    """
    if not start:
        return
    stack = []
    nodes = set()
    stack.append(start)
    nodes.add(start)
    print(start.value)
    while stack:
        cur = stack.pop()
        for node in cur.neighbors:
            if node not in nodes:
                stack.append(cur)
                stack.append(node)
                nodes.add(node)
                print(node.value)
                break


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
    dfs(graph.nodes[1])
    print('=' * 10)
    dfs2(graph.nodes[1])
