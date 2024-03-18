"""
2
"""
from datetime import datetime, timedelta


def next_second():
    print("请输入一个24小时制的时间（格式：HH:MM:SS）：")
    user_input = input().strip()
    try:
        # 解析用户输入的时间
        user_time = datetime.strptime(user_input, "%H:%M:%S")
        # 计算1秒后的时间
        nextsecond = user_time + timedelta(seconds=1)
        # 输出1秒后的时间
        print("1秒后的时间是：", nextsecond.strftime("%H:%M:%S"))
    except ValueError:
        # 最后，使用 `strftime` 方法将计算后的时间格式化为字符串并输出。如果用户输入的时间格式不符合要求，则会捕获 `ValueError` 异常并给出错误提示。
        print("输入的时间格式不正确，请按照HH:MM:SS格式输入。")


# next_second()

"""
3
"""


# 从word.txt中读取文本
def find_reverse_pairs(filename):
    # 读取word.txt文件，并按行分割成单词列表
    with open(filename, 'r') as file:
        words = set(file.read().splitlines())
    # 遍历单词列表
    for word in words:
        # 将当前单词反转并与已处理的单词集合进行比较
        if word[::-1] in words:
            # 如果找到反向对，则输出
            print(f"'{word}' 和 '{word[::-1]}' 是反向对")


# 调用函数，传入文件名
# find_reverse_pairs('word.txt')


"""
4
"""


def count_word_frequency(file_path):
    """
    计算一个英文单词组成的文本文件中各个单词出现的次数。
    参数:
    file_path (str): 文本文件路径
    返回:
    word_count_dict (dict): 字典，键为单词，值为对应的出现次数
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = text.split()
        word_count_dict = {}
        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
    return word_count_dict


# 测试用例
test_file = "shakespeare.txt"
result = count_word_frequency(test_file)
print(result)


def count_keyword_frequency(file_path, keywords):
    """
    统计一个英文单词组成的文本文件中给定关键词列表中各个单词出现的频率。
    参数:
    file_path (str): 文本文件路径
    keywords (list): 关键词列表
    返回:
    keyword_freq_dict (dict): 字典，键为关键词，值为对应的出现频率
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        keyword_freq_dict = {keyword: 0 for keyword in keywords}
        for word in words:
            if word in keyword_freq_dict:
                keyword_freq_dict[word] += 1
        for key in keyword_freq_dict:
            keyword_freq_dict[key] /= len(words)
        return keyword_freq_dict


# 测试用例
test_file = "shakespeare.txt"
keywords = ['the']
result = count_keyword_frequency(test_file, keywords)
print(result)
