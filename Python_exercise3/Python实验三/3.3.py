import random
import string


def markov_analysis(text, n):
    words = text.split()
    prefix_dict = {}

    for i in range(len(words) - n):
        prefix = tuple(words[i:i + n])
        suffix = words[i + n]
        if prefix in prefix_dict:
            prefix_dict[prefix].append(suffix)
        else:
            prefix_dict[prefix] = [suffix]

    return prefix_dict


def generate_text(prefix_dict, n, num_sentences):
    prefix = random.choice(list(prefix_dict.keys()))
    text = ' '.join(prefix)

    for _ in range(num_sentences):
        for _ in range(n):
            if prefix in prefix_dict:
                next_word = random.choice(prefix_dict[prefix])
                text += ' ' + next_word
                prefix = prefix[1:] + (next_word,)
            else:
                break

        # Add punctuation for sentence ending
        if text[-1] in string.punctuation:
            continue
        else:
            text += random.choice(['.', '!', '?']) + ' '
            prefix = random.choice(list(prefix_dict.keys()))

    return text.capitalize()


# 读取文本文件
with open('emma.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 设置阶数n
n = 5

# 进行马尔可夫文本分析
prefix_dict = markov_analysis(text, n)

# 生成随机文本
num_sentences = 3
random_text = generate_text(prefix_dict, n, num_sentences)
print(random_text)
