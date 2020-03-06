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


def compressString(self, S: str) -> str:
    """
    字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
    比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返
    回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）
    :param self:
    :param S:
    :return:
    """

    """
    第一次的错误思路是用截取最后一个字符作为数量没有考虑到数量大于10后占两位的情况
    """
    if S == '':
        return S

    autoList = []
    for i in range(0, len(S)):

        """
            s[i : i+1]是本次循环的字符
        """
        if i == 0:
            autoList.append(S[0])
            autoList.append('1')
        elif S[i:i + 1] == S[i - 1:i]:
            va = autoList[(len(autoList) - 1)]
            num = int(va) + 1
            autoList.pop()
            autoList.append(str(num))
        else:
            autoList.append(S[i:i + 1])
            autoList.append('1')

    finals = "".join(autoList)

    return finals if len(finals) < len(S) else S

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    """
    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
    :param self:
    :param head:
    :return:
    """
    set1 = set(head)
    list1 = list(set1)
    # str = str(set1)
    # list1 = list(eval(str))
    return list1



if __name__ == '__main__':
    # print(canPermutePalindrome(self='', s='tactcoa'))
    # print(oneEditAway(self='', first='teacher', second='teachy'))
    # print(compressString(self='',
    #                      S='rrrrLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLvvvvvvvvvvvKKKKKKKKKKKKKKiiiiiiiiiiiiiiiiiiiiiiiiiiiiZZZZZZZZZZZZZZZZZZZIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIoooooooooooooooooooooooooooooooooooobbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbvvvvvvvvvvvvvvvvvvvvvvvllllllllllllllllllllllllllllllllllllllllBBBBBBBKKKKKKKKKKKKKKfffffffffffffffffffffffffffffffffffDDDDDDDDDDDDDDDDDDDDDDDDDDDsssssssssssssssssssssssssssssssssssssssNNNNNZZZZZZZZZZZZZZZZZZZZZZZZZZNNNNNNNNNNDDDDDDDDDDDDDDDTTTTT'))

    print(removeDuplicateNodes(self='', head=[1, 1, 1, 2, 3]))
