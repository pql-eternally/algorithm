"""
输入正数数组costs、正数数组profits、正数K和正数M
costs[i]表示i号项目的花费
profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
K表示你只能串行的最多做k个项目
M表示你初始的资金
说明：每做完一个项目，马上获得的收益，可以支持你去做下一个项目，不能并行的做项目。
输出：最后获得的最大钱数
"""


class Program:
    profit: int
    cost: int

    def __init__(self, p: int, c: int):
        self.profit = p
        self.cost = c

    def __str__(self):
        return f'[{self.profit}, {self.cost}]'


def find_max_capital(k: int, m: int, costs: list, profits: list) -> int:
    programs = []
    for i in range(len(costs)):
        programs.append(Program(profits[i], costs[i]))
    min_cost_heap = sorted(programs, key=lambda p: p.cost)
    max_profit_heap = []
    for i in range(k):
        while min_cost_heap and min_cost_heap[0].cost <= m:
            max_profit_heap.append(min_cost_heap.pop(0))
        if not max_profit_heap:
            return m
        max_profit_heap.sort(key=lambda p: p.profit, reverse=True)
        program = max_profit_heap.pop(0)
        m += program.profit
    return m


def main():
    costs = [1, 2, 3, 4, 5]
    profits = [2, 4, 3, 1, 6]
    m = find_max_capital(3, 2, costs, profits)
    print(m)


if __name__ == '__main__':
    main()
