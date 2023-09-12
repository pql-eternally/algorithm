"""
说说下面代码的输出结果，并解释原因
"""

l1 = [1, 2, 3]

l2 = l1
l2.append(4)
print(l1)
print(l2)

l3 = l1[:]
l3.append(5)
print(l1)
print(l3)
