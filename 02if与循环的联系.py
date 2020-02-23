import random

target = random.randrange(1, 100)

num = 0
while True:
    if num == 5:
        print('没有机会了')
        break
    print(f'还剩{5-num}次机会')
    n = int(input('请猜一个1~100的整数:'))
    if n < target:
        print('菜鸡猜小了:)')
        num += 1
    elif n > target:
        print('你猜数猜的像cxk,大了:)')
        num += 1
    else:
        print('猜中了!!! 奖励你去给我拿一罐可乐:)')
        break
