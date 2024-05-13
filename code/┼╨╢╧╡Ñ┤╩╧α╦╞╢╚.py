from collections import Counter

def checkAndModify(word):
    # 待检测单词的字母频次
    fre = dict(Counter(word))
    # 待测单词中各字母频次与所有候选单词的距离，即字母频次之差
    similars = {w:[fre[ch]-words[w].get(ch,0) for ch in word]
                  +[words[w][ch]-fre.get(ch,0) for ch in w]
                for w in words}
    # 返回最接近的单词，即字母频次之差的平方和最小的单词
    return min(similars.items(),
               key=lambda item:sum(map(lambda i:i**2, item[1])))[0]

# 候选单词
words = {'good', 'hello', 'world', 'python', 'fuguo',
         'yantai', 'shandong', 'great'}

# 每个单词中字母频次，{'good':{'g':1, 'o':2, 'd':1}, 'hello':{...}, ...}
words = {word:dict(Counter(word)) for word in words}

# 测试
for word in ['god', 'hood', 'wello',
             'helo', 'pychon', 'guguo', 'shangdong']:
    print(word, ':', checkAndModify(word))
