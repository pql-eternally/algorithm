"""
try-except-else-finally
"""


def func(a):
    try:
        print('try')
        if a < 0:
            raise ValueError("data can not be negative")
    except ValueError as e:
        print("except")
        raise e
    else:
        print("else")
    finally:
        print("finally")
        return a


print(func(1))
print("=" * 20)
print(func(-1))
