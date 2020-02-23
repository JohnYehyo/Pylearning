# 函数
def fn1(a):
    a = 1
    print('a = ', a, id(a))


b = [1, 2, 3]
print('b = ', b, id(b))
fn1(b)


def fn2(c):
    print('c = ', c, type(c))


d = 1
e = [1, 2, 3]
f = (1, 2, 3)
g = {1, 2, 3}
fn2(d)
fn2(e)
fn2(f)
fn2(g)


# 可变参数及关键字参数的形式传递(可变参数不在最后时需要相应的传递关键字参数)
def fn3(x, *m, y):
    print('x = ', x)
    print('m = ', m)
    print('y = ', y)


fn3(1, 2, 3, 4, 5, ['a', 'b', 'c'], ('A', 'B', 'C'), {1, 2, 3}, y=123)


# 可变参数接收关键字参数
def fn4(**m):
    print('mm = ', m, type(m))


fn4(a=1, b=2, c=3)


# 遍历字典
def fn5(**m):
    return m


var1 = fn5(a=1, b=2, c=3)

for i in var1.keys():
    print(i, var1[i])
for i in var1.values():
    print(i)
for k, v in var1.items():
    print(k, '=', v)
