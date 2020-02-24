# 函数
# def fn1(a):
#     a = 1
#     print('a = ', a, id(a))
#
#
# b = [1, 2, 3]
# print('b = ', b, id(b))
# fn1(b)
#
#
# def fn2(c):
#     print('c = ', c, type(c))
#
#
# d = 1
# e = [1, 2, 3]
# f = (1, 2, 3)
# g = {1, 2, 3}
# fn2(d)
# fn2(e)
# fn2(f)
# fn2(g)


# 可变参数及关键字参数的形式传递(可变参数不在最后时需要相应的传递关键字参数)
# def fn3(x, *m, y):
#     print('x = ', x)
#     print('m = ', m)
#     print('y = ', y)


# fn3(1, 2, 3, 4, 5, ['a', 'b', 'c'], ('A', 'B', 'C'), {1, 2, 3}, y=123)


# 可变参数接收关键字参数
# def fn4(**m):
#     print('mm = ', m, type(m))


# fn4(a=1, b=2, c=3)


# 遍历字典
# def fn5(**m):
#     return m


# var1 = fn5(a=1, b=2, c=3)

# for i in var1.keys():
#     print(i, var1[i])
# for i in var1.values():
#     print(i)
# for k, v in var1.items():
#     print(k, '=', v)


"""
模块中的函数除了定义函数之外还有可以执行的代码,那么Python解释器会直接执行这些代码
如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话
除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才
是“__main__”。
"""

# 导入module1时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
import module1


# 函数中变量作用域问题
# 1.
# def foo():
#     b = 'hello'
#
#     def bar():  # Python中可以在函数内部再定义函数
#         c = True
#         print(a)
#         print(b)
#         print(c)
#
#     bar()
#     # print(c)  # NameError: name 'c' is not defined
#
#
# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()

# 2.
# def foo():
#     a = 200
#     print(a)  # 200
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 100

# 这里foo中是声明了一个a=200的局部变量, print(a) 也不会获取到他而是使用自己的局部变量a还为100,想要改变a的值输出200 可以设置全局变量

# def foo():
#     global a
#     a = 200
#     print(a)
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)
