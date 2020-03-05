s = "不使人间造孽孽孽钱"

# print(s[0])
# print(s[-1])
# print(s[0:])
# print(s[:2])
# print(s[0:3])
#反转
# print(s[::-1])

# # 步长限制取值
# print(s[0:5:3])

# # 替换
# print(s.replace("孽", "缘", 2))

# # 首字母大写
# print(s.capitalize())

# 某个字符在字符串中出现的次数
# print(s.count("孽", 0, 6))
# print(s.count("孽",))

# 大小写和去除空格
# ss = " abcAbc "
# print(ss.lower())
# print(ss.upper())
# print(ss.lstrip())
# print(ss.rstrip())
# print(ss.strip())
# print(ss.swapcase())

# 分割
sss = "a,b,c,d,e,f,g"
print(sss.split(","))
print(sss.split(",", 3))

# ss = '''<HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT TYPE=button VALUE=Back
# ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>'''
# print(ss)

#反转
#使用字符串切片的方法
print(sss[::-1])
#使用reversed()函数
print(''.join(reversed(sss)))