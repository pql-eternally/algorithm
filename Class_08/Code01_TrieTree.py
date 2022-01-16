"""
前缀树
"""


class Node(object):
    path: int = 0
    end: int = 0
    leaves: dict = None

    def __init__(self):
        self.path = 0
        self.end = 0
        self.leaves = {}


class TireTree(object):
    # 根节点
    root: Node = None

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        前缀树中加入word
        """
        node = self.root
        for c in word:
            if c not in node.leaves:
                node.leaves[c] = Node()
            node = node.leaves[c]
            node.path += 1
        node.end += 1

    def delete(self, word: str) -> None:
        """
        前缀树中删除word
        """
        if self.search(word) == 0:
            return
        node = self.root
        for c in word:
            # 如果只有一条路径删除当前节点，防止内存泄漏
            if node.leaves[c].path == 1:
                node.leaves.pop(c)
                return
            node = node.leaves[c]
            node.path -= 1
        node.end -= 1

    def search(self, word: str) -> int:
        """
        word这个单词之前加入过几次
        """
        node = self.root
        for c in word:
            if c not in node.leaves:
                return 0
            node = node.leaves[c]
        return node.end

    def prefix_num(self, word: str) -> int:
        """
        所有加入的字符串中，有几个是以pre这个字符串作为前缀的
        """
        node = self.root
        for c in word:
            if c not in node.leaves:
                return 0
            node = node.leaves[c]
        return node.path


def main():
    tree = TireTree()
    tree.insert('hello')
    tree.insert('he')
    tree.insert('hero')
    tree.insert('pql')
    tree.insert('pql')
    tree.insert('pangqilong')
    tree.insert('xueyuanyuan')
    tree.insert('pangliting')
    tree.insert('pangsishun')
    tree.insert('shiquanying')
    tree.insert('miduo')
    tree.insert('pql')
    res = tree.search('pql')
    print(res)
    tree.delete('pql')
    tree.delete('python')
    tree.delete('xueyuanyuan')
    res = tree.search('xueyuanyuan')
    print(res)
    res = tree.prefix_num('pangqi')
    print(res)


if __name__ == '__main__':
    main()
