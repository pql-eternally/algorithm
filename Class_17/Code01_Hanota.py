"""
汉诺塔游戏

左  中  右
"""


def hanuota(n: int):
    """
    @param n: 总共有多少个圆盘
    """
    return left_move_right(n)


def left_move_right(n):
    """
    从左柱子移动到右边柱子
    """
    if n == 1:
        print('Move 1 from left to right')
        return
    # 从左柱子移动n-1个圆盘到中间
    left_move_mid(n - 1)
    print(f'Move {n} from left to right')
    # 从中间柱子移动n-1个圆盘到右边
    mid_move_right(n - 1)


def left_move_mid(n):
    if n == 1:
        print('Move 1 from left to mid')
        return
    left_move_right(n - 1)
    print(f'Move {n} from left to mid')
    right_move_mid(n - 1)


def right_move_mid(n):
    if n == 1:
        print('Move 1 frm right to mid')
        return
    right_move_left(n - 1)
    print(f'Move {n} from right to mid')
    left_move_mid(n - 1)


def right_move_left(n):
    if n == 1:
        print('Move 1 frm right to left')
        return
    right_move_mid(n - 1)
    print(f'Move {n} from right to left')
    mid_move_left(n - 1)


def mid_move_left(n):
    if n == 1:
        print('Move 1 frm mid to left')
        return
    mid_move_right(n - 1)
    print(f'Move {n} from mid to left')
    right_move_left(n - 1)


def mid_move_right(n):
    if n == 1:
        print('Move 1 frm mid to right')
        return
    mid_move_left(n - 1)
    print(f'Move {n} from mid to right')
    left_move_right(n - 1)


def hanuota2(n: int):
    return from_move_to(n, 'left', 'right', 'mid')


def from_move_to(n, f, t, o):
    """
    @param n: 当前有多少个圆盘
    @param f: 从哪里移动的柱子
    @param t: 移动到哪里的柱子
    @param o: 另一个柱子
    @return:
    """
    if n == 1:
        print(f'Move 1 from {f} to {t}')
        return
    from_move_to(n - 1, f, o, t)
    print(f'Move {n} from {f} to {t}')
    from_move_to(n - 1, o, t, f)


def main():
    hanuota(3)
    print('=' * 10)
    hanuota2(3)


if __name__ == '__main__':
    main()
