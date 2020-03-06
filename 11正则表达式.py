import re
import traceback

phonePattern = re.compile(r'1[3456789]\d{9}')


def user():
    """
     验证输入用户名和QQ号是否有效并给出对应的提示信息

    要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
    :return:
    """
    username = input('请输入用户名:')
    qqmum = input('请输入QQ号:')

    flag1 = re.match(r'^\w{6,20}$', username)
    flag2 = re.match(r'^[1-9]\d{4,11}$', qqmum)

    if not flag1:
        print('用户名错误!')
    if not flag2:
        print('QQ号错误')
    if flag1 and flag2:
        print('正确!')


def phone():
    """
    从一段文字中提取出国内手机号码。
    :return:
    """

    # 创建正则表达式对象
    pattern = re.compile(r'^1[3456789]\d{9}$')
    text = '13380900998'
    # 1 查找所有匹配结果并保存到列表
    mylist = re.findall(pattern, text)
    print(mylist)

    # 2 循环取出匹配对象并打印内容
    for i in pattern.finditer(text):
        print(i.group())

    # 3 通过search函数指定搜索位置查找匹配对象
    m = pattern.search(text)
    while m:
        print(m.group())
        m = pattern.search(text, m.end())


def phoneAction():
    """
    拆分匹配文本中的手机号码并写到新文本
    :return:
    """
    try:
        with open('phone.txt', 'r', encoding='UTF-8') as info:
            for line in info:
                for i in phonePattern.finditer(line):
                    with open('realPhone.txt', 'a') as phone:
                        phone.write(i.group() + '\n')
    except Exception:
        traceback.print_exc()


def replace():
    text = '三年二班周杰伦 strong!'
    parttern1 = re.compile('[二周杰伦strong]')
    parttern2 = re.compile('[二周]|strong[!]|杰[伦]')
    parttern3 = re.compile('[二班]|周杰伦')
    newText1 = re.sub(parttern1, "*", text)
    newText2 = re.sub(parttern2, "*", text)
    newText3 = re.sub(parttern3, "*", text)
    print(newText1)
    print(newText2)
    print(newText3)



if __name__ == '__main__':
    # user()
    # phone()
    replace()
