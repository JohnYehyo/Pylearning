def canPermutePalindrome(self, s: str) -> bool:
    """
    给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

    回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

    回文串不一定是字典当中的单词。
    """

    arr = []
    for i in s:
        if i not in arr:
            arr.append(i)
        else:
            arr.remove(i)
    if len(arr) > 1:
        return False
    return True


def oneEditAway(self, first: str, second: str) -> bool:
    """
    字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
    """

    if abs(len(first) - len(second)) > 1:
        return False
    if len(first) == len(second):
        for i in range(0, len(second) - 1):
            if first[i] != second[i]:
                new_str = second[0:i] + first[i] + second[i + 1:]
                if first == new_str:
                    return True
                return False
        return True
    if len(first) > len(second):
        for i in range(0, len(first) - 1):
            if first[i] != second[i]:
                new_str = second[0:i] + first[i] + second[i:]
                if new_str == first:
                    return True
                return False
        return True
    else:
        for i in range(0, len(second) - 1):
            if second[i] != first[i]:
                new_str = first[0:i] + second[i] + first[i:]
                if new_str == second:
                    return True
                return False
        return True


if __name__ == '__main__':
    print(canPermutePalindrome(self='', s='tactcoa'))
    # print(oneEditAway(self='', first='teacher', second='teachy'))
