"""
员工信息的定义如下:
class Employee {
    public int happy; // 这名员工可以带来的快乐值
    List<Employee> subordinates; // 这名员工有哪些直接下级
}
公司的每个员工都符合 Employee 类的描述。整个公司的人员结构可以看作是一棵标准的、 没有环的多叉树
树的头节点是公司唯一的老板，除老板之外的每个员工都有唯一的直接上级
叶节点是没有任何下属的基层员工(subordinates列表为空)，除基层员工外每个员工都有一个或多个直接下级
这个公司现在要办party，你可以决定哪些员工来，哪些员工不来，规则：
1.如果某个员工来了，那么这个员工的所有直接下级都不能来
2.派对的整体快乐值是所有到场员工快乐值的累加
3.你的目标是让派对的整体快乐值尽量大
给定一棵多叉树的头节点boss，请返回派对的最大快乐值。
"""


class Employee:
    happy: int
    subordinates: list

    def __init__(self, h):
        self.happy = h
        self.subordinates = []


class Info:
    yes: int
    no: int

    def __init__(self, y: int, n: int):
        self.yes = y
        self.no = n


def process(node: Employee):
    """
    flag: true 当前员工来  false 当前员工不来
    """
    if not node:
        return Info(0, 0)
    yes = node.happy
    no = 0
    for employee in node.subordinates:
        info = process(employee)
        yes += info.no
        no += max(info.yes, info.no)
    return Info(yes, no)


def max_happy(boss: Employee):
    info = process(boss)
    return max(info.yes, info.no)


def main():
    boss = Employee(20)
    ceo = Employee(3)
    cto = Employee(100)
    cfo = Employee(60)
    cfo.subordinates = [Employee(33), Employee(22), Employee(55)]
    boss.subordinates = [ceo, cto, cfo]
    res = max_happy(boss)
    print(res)


if __name__ == '__main__':
    main()
