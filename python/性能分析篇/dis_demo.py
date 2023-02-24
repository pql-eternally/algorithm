"""
dis模块可以分析函数的字节码，我们可以了解函数的实际执行过程，包括变量的创建和操作、条件分支和循环等操作。
这些信息可以帮助我们优化程序的性能，尤其是对于一些复杂的函数和算法，使用 dis 模块进行分析可以更好地理解它们的执行过程。

指令集：
LOAD_CONST: 将常量加载到堆栈上
LOAD_FAST: 将局部变量加载到堆栈上
STORE_FAST: 将堆栈顶部的值存储到局部变量中
LOAD_GLOBAL: 将全局变量加载到堆栈上
STORE_GLOBAL: 将堆栈顶部的值存储到全局变量中
LOAD_METHOD: 将方法加载到堆栈上
CALL_METHOD: 调用方法
POP_TOP: 弹出堆栈顶部的元素
DUP_TOP: 复制堆栈顶部的元素
ROT_TWO: 交换堆栈顶部的两个元素
ROT_THREE: 将第三个元素移到堆栈顶部
JUMP_FORWARD: 跳转到指定位置
JUMP_IF_FALSE_OR_POP: 如果堆栈顶部的元素为假值，则跳转到指定位置
JUMP_ABSOLUTE: 跳转到指定位置
RETURN_VALUE: 返回堆栈顶部的值
COMPARE_OP: 比较操作
LOAD_NAME: 将变量名加载到堆栈上。
STORE_NAME: 将堆栈顶部的值存储到变量名中。
LOAD_ATTR: 获取对象属性，并将其加载到堆栈上。
STORE_ATTR: 将堆栈顶部的值存储到对象属性中。
BINARY_AND: 对两个堆栈顶部的元素进行按位与操作。
BINARY_OR: 对两个堆栈顶部的元素进行按位或操作。
BINARY_XOR: 对两个堆栈顶部的元素进行按位异或操作。
INPLACE_ADD: 对堆栈顶部的两个元素进行就地加法操作。
INPLACE_SUBTRACT: 对堆栈顶部的两个元素进行就地减法操作。
INPLACE_MULTIPLY: 对堆栈顶部的两个元素进行就地乘法操作。
INPLACE_DIVIDE: 对堆栈顶部的两个元素进行就地除法操作。
UNARY_NOT: 对堆栈顶部的元素进行逻辑非操作。
MAKE_FUNCTION: 创建一个新的函数对象。
CALL_FUNCTION: 调用函数。
JUMP_IF_TRUE_OR_POP: 如果堆栈顶部的元素为真值，则跳转到指定位置。
SETUP_LOOP: 设置一个循环块。
POP_BLOCK: 弹出代码块。
SETUP_WITH: 设置一个 with 块。
WITH_CLEANUP_START: 开始一个 with 块的清理操作。
WITH_CLEANUP_FINISH: 完成一个 with 块的清理操作。
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
