"""
下面的代码会输出什么？请解释原因。
"""


def extend_list(val, items=[]):  # noqa
    items.append(val)
    return items


list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')
print(list1)
print(list2)
print(list3)
