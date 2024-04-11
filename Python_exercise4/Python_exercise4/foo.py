import timeit
import re
import tkinter

"""5(1)"""


def rotateword(strsrc, n):
    strdes = ''
    for c in strsrc:
        if c.isalpha():
            if c.islower():
                c = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            else:
                c = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        strdes += c
    return strdes


def rotate_word_optimized(strsrc, n):
    a_ord = ord('a')
    A_ord = ord('A')
    return ''.join([
        chr((ord(c) - a_ord + n) % 26 + a_ord) if c.islower() else
        chr((ord(c) - A_ord + n) % 26 + A_ord) if c.isupper() else c
        for c in strsrc
    ])


"""5(2)"""


def avoid_1(strsrc, avoid_lst):
    for c in avoid_lst:
        if c in strsrc:
            return True
    return False


def avoid_2(strsrc, avoid_lst):
    return bool(set(strsrc) & set(avoid_lst))


def avoid_3(strsrc, avoid_lst):
    return any(c in strsrc for c in avoid_lst)


def avoid_4(strsrc, avoid_lst):
    # 将 avoid_lst 中的每个字符转义并以 "|" 连接，构成正则表达式
    pattern = '|'.join(re.escape(c) for c in avoid_lst)
    # 检查字符串中是否存在 avoid_lst 中的任一字符
    return bool(re.search(pattern, strsrc))


def useonly(strsrc, use_lst):
    # 创建一个包含 use_lst 中所有字符的正则表达式
    # 注意：如果字符列表中包含特殊字符，我们需要对它们进行转义
    pattern = f"[^{re.escape(''.join(use_lst))}]"
    # 使用 re.search() 检查是否存在不在 use_lst 中的字符
    if re.search(pattern, strsrc):
        # 如果找到了匹配，意味着 strsrc 包含至少一个不在 use_lst 中的字符
        return False
    # 如果没有找到匹配，意味着所有字符都在 use_lst 中
    return True


"""5(4)"""

import re


def useall(word, needed_letters):
    # 构建正则表达式，匹配单词中包含所有需要字母至少一个的情况
    pattern = ''.join(f"(?=.*{letter})" for letter in needed_letters)
    pattern += '.*'  # 匹配任意其他字符
    # 使用 re.search() 函数查找匹配
    return bool(re.search(pattern, word))


def words_with_all_vowels(file_path):
    with open(file_path, 'r') as file:
        for word in file:
            word = word.strip()
            if useall(word, 'aeiou'):
                print(word)


"""5(5)"""


def hasnoe(word):
    # 使用正则表达式匹配是否包含字母 'e'
    return not re.search(r'e', word)


def percentage_without_e(file_path):
    total_words = 0
    words_without_e = 0

    with open(file_path, 'r') as file:
        # 使用列表推导式一次性读取所有单词并进行计算
        words = [word.strip() for word in file]
        total_words = len(words)
        words_without_e = sum(1 for word in words if 'e' not in word)

    if total_words == 0:
        return 0
    else:
        return (words_without_e / total_words) * 100


"""5(6)"""


def isabecedarian(word):
    # 使用正则表达式匹配是否满足字母表序
    return bool(re.match(r'^a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*$', word))


def get_abecedarian_words(file_path):
    with open(file_path, 'r') as file:
        # 使用列表推导式一次性读取所有单词并进行筛选
        abecedarian_words = [word.strip() for word in file if isabecedarian(word.strip())]

    return abecedarian_words
