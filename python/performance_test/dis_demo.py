"""
dis模块可以分析函数的字节码，我们可以了解函数的实际执行过程，包括变量的创建和操作、条件分支和循环等操作。
这些信息可以帮助我们优化程序的性能，尤其是对于一些复杂的函数和算法，使用 dis 模块进行分析可以更好地理解它们的执行过程。

指令集：
LOAD_CONST: 将常量加载到堆栈上
LOAD_FAST: 将局部变量加载到堆栈上
LOAD_GLOBAL: 将全局变量加载到堆栈上
LOAD_METHOD: 将方法加载到堆栈上
LOAD_NAME: 将变量名加载到堆栈上
LOAD_ATTR: 获取对象属性，并将其加载到堆栈上
LOAD_CLOSURE: 将闭包变量加载到堆栈上
LOAD_DEREF: 将闭包变量加载到堆栈上

STORE_FAST: 将堆栈顶部的值存储到局部变量中
STORE_GLOBAL: 将堆栈顶部的值存储到全局变量中
STORE_NAME: 将堆栈顶部的值存储到变量名中
STORE_ATTR: 将堆栈顶部的值存储到对象属性中
STORE_MAP: 将堆栈顶部的值存储到字典中
STORE_DEREF: 将堆栈顶部的值存储到闭包变量中

CALL_METHOD: 调用方法
CALL_FUNCTION: 调用函数
RETURN_VALUE: 返回堆栈顶部的值
MAKE_FUNCTION: 创建一个新的函数对象

SETUP_LOOP: 设置一个循环块
POP_BLOCK: 弹出代码块
POP_TOP: 弹出堆栈顶部的元素
DUP_TOP: 复制堆栈顶部的元素
ROT_TWO: 交换堆栈顶部的两个元素
ROT_THREE: 将第三个元素移到堆栈顶部
JUMP_FORWARD: 跳转到指定位置
JUMP_ABSOLUTE: 跳转到指定位置
JUMP_IF_FALSE_OR_POP: 如果堆栈顶部的元素为假值，则跳转到指定位置

COMPARE_OP: 比较操作
BINARY_AND: 对两个堆栈顶部的元素进行按位与操作
BINARY_OR: 对两个堆栈顶部的元素进行按位或操作
BINARY_XOR: 对两个堆栈顶部的元素进行按位异或操作
INPLACE_ADD: 对堆栈顶部的两个元素进行就地加法操作
INPLACE_SUBTRACT: 对堆栈顶部的两个元素进行就地减法操作
INPLACE_MULTIPLY: 对堆栈顶部的两个元素进行就地乘法操作
INPLACE_DIVIDE: 对堆栈顶部的两个元素进行就地除法操作
UNARY_NOT: 对堆栈顶部的元素进行逻辑非操作

SETUP_WITH: 设置一个with块
WITH_CLEANUP_START: 开始一个with块的清理操作
WITH_CLEANUP_FINISH: 完成一个with块的清理操作
"""
import dis
import functools
import time


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


def decorator(f):
    """
    118           0 LOAD_GLOBAL              0 (functools)
                  2 LOAD_METHOD              1 (wraps)
                  4 LOAD_DEREF               0 (f)
                  6 CALL_METHOD              1

    119           8 LOAD_CLOSURE             0 (f)
                 10 BUILD_TUPLE              1
                 12 LOAD_CONST               1 (<code object wrapper at 0x10f58d030, file "/Users/qhkjit/Develop/algorithm/python/performance_test/dis_demo.py", line 118>)
                 14 LOAD_CONST               2 ('decorator.<locals>.wrapper')
                 16 MAKE_FUNCTION            8 (closure)
                 18 CALL_FUNCTION            1
                 20 STORE_FAST               1 (wrapper)

    126          22 LOAD_FAST                1 (wrapper)
                 24 RETURN_VALUE

    Disassembly of <code object wrapper at 0x10f58d030, file "/Users/qhkjit/Develop/algorithm/python/performance_test/dis_demo.py", line 118>:
    120           0 LOAD_GLOBAL              0 (time)
                  2 LOAD_METHOD              0 (time)
                  4 CALL_METHOD              0
                  6 STORE_FAST               2 (t1)

    121           8 LOAD_DEREF               0 (f)
                 10 LOAD_FAST                0 (args)
                 12 BUILD_MAP                0
                 14 LOAD_FAST                1 (kwargs)
                 16 DICT_MERGE               1
                 18 CALL_FUNCTION_EX         1
                 20 STORE_FAST               3 (res)

    122          22 LOAD_GLOBAL              0 (time)
                 24 LOAD_METHOD              0 (time)
                 26 CALL_METHOD              0
                 28 STORE_FAST               4 (t2)

    123          30 LOAD_GLOBAL              1 (print)
                 32 LOAD_CONST               1 ('Run time: ')
                 34 LOAD_FAST                4 (t2)
                 36 LOAD_FAST                2 (t1)
                 38 BINARY_SUBTRACT
                 40 FORMAT_VALUE             0
                 42 LOAD_CONST               2 ('s')
                 44 BUILD_STRING             3
                 46 CALL_FUNCTION            1
                 48 POP_TOP

    124          50 LOAD_FAST                3 (res)
                 52 RETURN_VALUE

    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        print(f'Run time: {t2 - t1}s')
        return res

    return wrapper


def func_with():
    with open('./dis_demo.py', 'r') as f:
        data = f.readline()
        print(data)
        return


if __name__ == '__main__':
    # dis.dis(func)
    # dis.dis(func2)
    # dis.dis(decorator)
    dis.dis(func_with)
