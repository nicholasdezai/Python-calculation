def correct_i(text):
    # 将单独的字母 "i" 替换为大写的 "I"
    corrected_text = text.replace(' i ', ' I ')
    corrected_text = corrected_text.replace(' i,', ' I,')  # 处理逗号后的情况
    corrected_text = corrected_text.replace(' i.', ' I.')  # 处理句号后的情况
    corrected_text = corrected_text.replace(' i!', ' I!')  # 处理感叹号后的情况
    corrected_text = corrected_text.replace(' i?', ' I?')  # 处理问号后的情况

    # 如果 "i" 在句子开头，替换为大写 "I"
    corrected_text = corrected_text.replace('i ', 'I ')
    # 如果 "i" 在句子结尾，替换为大写 "I"
    corrected_text = corrected_text.replace(' i', ' I')
    # 如果 "i" 是整个句子，替换为大写 "I"
    corrected_text = corrected_text.replace('i', 'I')

    return corrected_text


# 示例文本
example_text = "i love programming. it is fun and interesting. i am happy with my work."

# 纠正拼写错误并输出结果
corrected_text = correct_i(example_text)
print("纠正后的文本：", corrected_text)


def correct_i(text):
    # 将单词中的字母 "1" 替换为 "i"
    corrected_text = text.replace('1', 'i')

    return corrected_text


# 示例文本
example_text = "Th1s 1s an example of a sentence w1th m1sspell1ng."

# 纠正拼写错误并输出结果
corrected_text = correct_i(example_text)
print("纠正后的文本：", corrected_text)

import re


def remove_repeated_words(text):
    # 使用正则表达式查找连续重复的单词
    pattern = r'\b(\w+)\s+\1\b'
    # 将连续重复的单词替换为单个单词
    corrected_text = re.sub(pattern, r'\1', text)
    return corrected_text


# 示例文本
example_text = "This is is a test test sentence. Please Pvlease correct it."

# 检查并修复连续重复的单词，并输出结果
corrected_text = remove_repeated_words(example_text)
print("修正后的文本：", corrected_text)


# 4，编写程序,用户输入一段英文,然后输出这有段英文中所有长度为3个字母的时网。
def find_three_letter_words(text):
    # 使用正则表达式找出所有的单词
    words = re.findall(r'\b\w{3}\b', text)

    return words


# 输入提示用户输入英文文本
input_text = input("请输入一段英文文本：")

# 调用函数并获取结果
result = find_three_letter_words(input_text)

# 输出所有长度为3的单词
print("长度为3个字母的单词有：", result)
