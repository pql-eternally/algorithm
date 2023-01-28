"""
请把一段纸条竖着放在桌子上，然后从纸条的下边向上方对折1次，压出折痕后展开
此时折痕是凹下去的，即折痕突起的方向指向纸条的背面
如果从纸条的下边向上方连续对折2次，压出折痕后展开
此时有三条折痕，从上到下依次是下折痕、下折痕和上折痕。
给定一个输入参数N，代表纸条都从下边向上方连续对折N次
请从上到下打印所有折痕的方向。
N=1时，打印: down
N=2时，打印: down down up
"""


def print_all_folds(n: int):
    process(1, n, True)
    print()


def process(i: int, n: int, down: bool):
    if i > n:
        return
    process(i + 1, n, True)
    print('凹' if down else '凸', end=',')
    process(i + 1, n, False)


def main():
    print_all_folds(1)
    print_all_folds(2)
    print_all_folds(3)


if __name__ == '__main__':
    main()
