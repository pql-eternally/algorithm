# 引发异常所在上下文的信息
# BaseException.__context__
# BaseException.__cause__
# BaseException.__suppress_context__
# BaseException.__traceback__
import sys


class MyException(Exception):
    pass


def test_with_traceback():
    try:
        raise MyException('value error occurred')
    except MyException:
        tb = sys.exception().__traceback__
        raise ValueError(...).with_traceback(tb)
