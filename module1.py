def foo():
    pass
    print('foo!')


def bar():
    pass


# 这样调用改模块会直接执行以下方法
# print('call foo()')
# foo()
# print('call bar()')
# bar()


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()

# 这样也会执行
# if __name__ == 'module1':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()
