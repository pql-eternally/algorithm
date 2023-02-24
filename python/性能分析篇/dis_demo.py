"""
dis模块可以分析函数的字节码，我们可以了解函数的实际执行过程，包括变量的创建和操作、条件分支和循环等操作。
这些信息可以帮助我们优化程序的性能，尤其是对于一些复杂的函数和算法，使用 dis 模块进行分析可以更好地理解它们的执行过程。
"""
import dis


def func():
    """
    执行结果
      字节码指令、操作数和注释信息
      5           0 LOAD_CONST               1 (2)
                  2 STORE_FAST               0 (x)

      6           4 LOAD_CONST               2 (3)
                  6 STORE_FAST               1 (y)

      7           8 LOAD_FAST                0 (x)
                 10 LOAD_FAST                1 (y)
                 12 BINARY_ADD
                 14 STORE_FAST               2 (z)

      8          16 LOAD_FAST                2 (z)
                 18 RETURN_VALUE
    """
    x = 2
    y = 3
    z = x + y
    return z


def func2(a, b):
    """
    33        0 LOAD_FAST                1 (b)
              2 LOAD_FAST                0 (a)
              4 ROT_TWO
              6 STORE_FAST               0 (a)
              8 STORE_FAST               1 (b)

    34       10 LOAD_FAST                0 (a)
             12 LOAD_FAST                1 (b)
             14 BUILD_TUPLE              2
             16 RETURN_VALUE
    """
    a, b = b, a
    return a, b


if __name__ == '__main__':
    # dis.dis(func)
    dis.dis(func2)
