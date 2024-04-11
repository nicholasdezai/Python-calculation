def read_words(file_path):
    """从给定文件读取单词，返回一个集合"""
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())


def is_reducible(word, word_set, cache):
    """递归检查单词是否是可缩减的"""
    if word in cache:  # 如果单词已在缓存中，直接返回结果
        return cache[word]
    if len(word) == 1:  # 基准情况
        return word in ('a', 'i')  # 只有'a'和'i'是有效的单字母单词
    # 尝试移除每个字母，检查剩余字符串是否是一个可缩减的单词
    for i in range(len(word)):
        sub_word = word[:i] + word[i + 1:]
        if sub_word in word_set and is_reducible(sub_word, word_set, cache):
            cache[word] = True  # 存储结果在缓存中
            return True
    cache[word] = False
    return False


def find_longest_reducible_word(word_set):
    """在给定的单词集合中找到最长的可缩减单词"""
    cache = {}  # 用于缓存已找到的可缩减单词
    longest_word = ''
    for word in word_set:
        if is_reducible(word, word_set, cache) and len(word) > len(longest_word):
            longest_word = word
    longest = []
    for word in word_set:
        if word in cache and cache.get(word):
            longest.append(word)
    longest.sort(key=lambda x: len(x), reverse=True)
    print(longest)
    return longest_word


file_path = 'words.txt'
word_set = read_words(file_path)
word_set.add('a')
word_set.add('i')
longest_word = find_longest_reducible_word(word_set)
print(f"The longest reducible word is: {longest_word}")
