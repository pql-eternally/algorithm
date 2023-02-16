"""
括号是否平衡，即左右括号是否匹配
"""
import random
import logging

from data_structures.stack.list_stack import Stack

logger = logging.getLogger(__name__)

parentheses_map = {
    ")": "(",
    "]": "[",
    "}": "{",
}


def is_parentheses_balanced(parentheses: str) -> bool:
    """
    校验给定的字符串是否括号平衡
    >>> is_parentheses_balanced("([]{})")
    True
    >>> is_parentheses_balanced("[()]{}{[()()]()}")
    True
    >>> is_parentheses_balanced("[(])")
    False
    """
    stack = Stack[str](len(parentheses))
    for char in parentheses:
        if char in parentheses_map.values():
            stack.push(char)
        elif char in parentheses_map:
            if stack.is_empty() or parentheses_map[char] != stack.pop():
                return False
    return stack.is_empty()


# 使用对数器进行测试
def generate_random_parentheses(length: int) -> str:
    parentheses = ["(", ")", "[", "]", "{", "}"]
    return "".join(random.choices(parentheses, k=length))


def comparator(parentheses: str) -> bool:
    """
    比较器，使用字符串替换方式实现
    """
    while "()" in parentheses or "[]" in parentheses or "{}" in parentheses:
        parentheses = parentheses.replace("()", "").replace("[]", "").replace("{}", "")
    return not parentheses


def main():
    for _ in range(10000):
        length = random.randint(0, 100)
        parentheses = generate_random_parentheses(length)
        print(f"Generator parentheses: {parentheses}")
        assert is_parentheses_balanced(parentheses) == comparator(parentheses)


if __name__ == '__main__':
    main()
