import random


def magic_trick():
    print("欢迎参加猜数字魔术游戏！")
    print("请在心中想一个1到100之间的数字，并不要告诉我。")
    input("准备好了吗？按下任意键开始游戏......")
    low = 1
    high = 100
    count = 0
    while True:
        count += 1
        guess = random.randint(low, high)
        print("我猜你心里想的数字是：", guess)
        answer = input("如果猜对了，请输入'y'；如果猜错了，请输入'h'表示猜的数字太高，或输入'l'表示猜的数字太低： ")
        if answer == 'y':
            print("哈哈，我猜对了，你心里想的数字是：", guess)
            print("我猜了", count, "次才猜对，不错吧！")
            break
        elif answer == 'h':
            high = guess - 1
        elif answer == 'l':
            low = guess + 1
        else:
            print("无效的输入，请重新输入。")


magic_trick()
