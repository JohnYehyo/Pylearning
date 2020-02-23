# 列表
# list01 = ["a", 'b']
# print(list01)

# 两种增加元素的方法
# list01.extend('x')
# print(list01)
# list01.insert(2, 'y')
# print(list01)

# 两种删除元素的方法
# del list01[0]
# print(list01)
#
# list01.remove('b')
# print(list01)

# list02 = ["c", "d"]
# # print(list01 + list02)
# # print(list01 * 2)
# list01.extend(list02)
# print(list01)

# 查找
# print(list01.index('b'))

# for循环
# for i in list01:
#     print(i)

# 元组
# tup1 = ()
# print(tup1)
# tup2 = (0,)
# print(tup2)
# tup3 = (0, "1a", 2)
# print(tup3)
# print(tup3[2])
# del tup2
# print(tup2)

# 集合
# ss = {1, 1, 22, 3}
# print(ss)
# ss.add(5)
# ss.add(1)
# print(ss)
# setset = set([111, 222, 3, 3, 33])
# print(setset)


# 字典:dict
d = {'a': '叶', 'b': '佳', 'c': '楠'}
# print(d)
# print(len(d))
# ddd = [('a', '叶', 'b', '佳', 'c', '楠'), ('a', '楠', 'b', '佳', 'c', '叶'), ('a', '叶', 'b', '楠', 'c', '佳')]
# print(ddd)
# print(len(ddd))

# 循环
# for i in ddd.keys():
#     print(i, ddd[i], end='')
# print()
# for i in d.values():
#     print(i, end='')
# print()
# for k, v in d.items():
#     print(k, '=', v)
# print()

# 添加
d['d'] = "!"
print(d)
d['d'] = "$"
print(d)

# 删除
# print(d.pop('b'))
# print(d.pop('bb', '没有这个值!'))
# print(d)
print(d.popitem())
print(d)
print(d.clear())
print(d)

