# DemoBool.py
# 얕은 복사

from re import A


a = [1, 2, 3]
b = a
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

print("----깊은복사----")
a = [1, 2, 3]
b = a[:]
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

#다른형식
import copy
a = [100, 200, 300]
b = copy.deepcopy(a)
a[0] = 3131
print(a)
print(b)
print(id(a), id(b))