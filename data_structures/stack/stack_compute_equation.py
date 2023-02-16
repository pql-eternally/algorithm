"""
使用Dijkstra的双堆栈算法来求解方程
例如：(5 + ((4 * 2) * (2 + 3)))
计算规则：
规则1：从左到右扫描表达式。当遇到操作数时，将其推到操作数堆栈上。
规则2：当在表达式中遇到运算符时，将其推到操作符堆栈上。
规则3：当表达式中遇到左括号时，请忽略它。
规则4：当表达式中遇到正确的括号时，弹出一个运算符堆栈中的运算符。它必须的两个操作数操作必须是推送到操作数堆栈的最后两个操作数。
    因此，我们弹出操作数堆栈两次，执行操作，并将结果推回操作数堆栈，以便可用用作从运算符堆栈中弹出的下一个运算符的操作数。
规则5：当扫描整个内缀表达式时，剩余的值操作数堆栈表示表达式的值。
"""
import operator as op
from typing import Callable

from data_structures.stack.list_stack import Stack

operators = {
    "*": op.mul,
    "/": op.truediv,
    "+": op.add,
    "-": op.sub
}


def compute_equation(equation: str) -> int:
    """
    >>> compute_equation("(5 + ((4 * 2) * (2 + 3)))")
    45
    """
    # 运算符堆栈
    operator_stack = Stack[Callable]()
    # 操作数堆栈
    operand_stack = Stack[int]()
    for char in equation:
        # 规则1：操作数入堆栈
        if char.isdigit():
            operand_stack.push(int(char))
        # 规则2：运算符
        elif char in operators:
            operator_stack.push(operators[char])
        # 规则3：忽略左括号
        elif char == "(":
            continue
        # 规则4：进行运算
        elif char == ")":
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operand_stack.push(operator(operand1, operand2))
    # 规则5：返回结果
    return operand_stack.pop()
