# 1. if-else
# a = 6
# if a < 5:
#     print("小于5")
# elif a == 5:
#     print("等于5")
# else:
#     print("大于5")

# 2. for循环
# for i in range(10):
#     print(f'for循环{i}轮')

# for i in range(1, 10, 3):
#     print(f'for循环{i}轮')

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}*{i}={i * j}', end=' ')
#     print()

# 3. while 循环
# n = 0
# while n < 5:
#     print(n)
#     n = n + 1

# n = 1
# while n < 10:
#     m = 1
#     while m <= n:
#         print(f'{m}*{n}={m * n}', end=' ')
#         m = m + 1
#     n += 1
#     print()

# 4. continue和break
# i = 0
# for i in range(0, 10):
#     if i % 2 == 0:
#         continue
#     print(i)

i = 0
for i in range(0, 10):
    if i == 6:
        break
    print(i)
