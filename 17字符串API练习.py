s = 'hello python!'
# 计算长度
print(len(s))
# 字符串首字母大写的副本
print(s.capitalize())
# 字符串中每个单词首字母与都大写的副本
print(s.title())
# 字符串全部大写的副本
print(s.upper())
# 查找子字符串在字符串中的位置
print(s.find('o'))
print(s.find('x'))
print(s.rfind('o'))
print(s.index('o'))
# 找不到时会产生异常
# print(s.index('x'))
# 判断字符串是否已指定的字符串开头和结尾
print(s.startswith('he'))
print(s.endswith('on!'))
# 以指定宽度居中字符串并在两侧填充指定的字符
print(s.center(20, '$'))
# 字符串靠右并在左侧填充指定的字符
print(s.rjust(20, '$'))
# 字符串靠左并在右侧填充指定的字符
print(s.ljust(20, '$'))
# 检查字符串是否由数字构成
print(s.isdigit())
# 检查字符串是否由字母构成
print(s.isalpha())
# 检查字符串是否由数字或字母构成
print(s.isalnum())
# 去除字符串两端的空格
print(s.strip())
# 去除字符串中的空格
print(s.replace(' ', ''))
# 替换
print(s.replace('o', 'j'))
print(s.replace('o', 'j', 1))
# 获取字符串中的字符
print(s[0])
print(s[0:])
print(s[:])
print(s[0:1])
print(s[:1])
# 类似于redis list结构的取值
print(s[0:-1])
# 反转
print(s[::-1])