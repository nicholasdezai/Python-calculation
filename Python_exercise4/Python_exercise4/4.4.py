import jieba
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import fontManager
import tkinter as tk
from tkinter import simpledialog, messagebox
from collections import Counter

matplotlib.rc("font", family='AR PL UMing CN')
fonts = set([f.name for f in fontManager.ttflist])
print(fonts)
if 'Noto Mono' not in fonts:
    print("没有找到合适的字体")
full_text = ""


def count_frequency(text, use_word=True):
    if use_word:
        tokens = jieba.lcut(text)
    else:
        tokens = list(text)
    return Counter(tokens)


def read_and_split_chapters(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    import re
    chapters = re.split(r'\-{50,}', text)
    return chapters


def main_analysis(filename, common_words):
    global full_text
    chapters = read_and_split_chapters(filename)
    full_text = ' '.join(chapters)  # 更新全文文本

    first_80 = ' '.join(chapters[:80])
    last_40 = ' '.join(chapters[-40:])

    freq_first_80 = {word: count_frequency(first_80, use_word=True)[word] for word in common_words}
    freq_last_40 = {word: count_frequency(last_40, use_word=True)[word] for word in common_words}

    with open('analysis_results.txt', 'w', encoding='utf-8') as f:
        f.write("前80回词频:\n")
        for word, count in freq_first_80.items():
            f.write(f"{word}: {count}\n")
        f.write("\n后40回词频:\n")
        for word, count in freq_last_40.items():
            f.write(f"{word}: {count}\n")


def plot_frequency():
    with open('analysis_results.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    words = []
    freqs_80 = []
    freqs_40 = []
    is_first_80 = True

    for line in lines:
        if '前80回' in line:
            continue
        elif '后40回' in line:
            is_first_80 = False
            continue
        if line.strip():
            word, freq = line.split(':')
            if is_first_80:
                words.append(word.strip())
                freqs_80.append(int(freq.strip()))
            else:
                freqs_40.append(int(freq.strip()))

    x = range(len(words))
    plt.bar(x, freqs_80, width=0.4, label='before 80 chapters')
    plt.bar([i + 0.4 for i in x], freqs_40, width=0.4, label='after 40 chapters', )
    plt.xlabel('词')
    plt.ylabel('频率')
    plt.title('词频对比')
    plt.xticks([i + 0.2 for i in x], words)
    plt.legend()
    plt.show()


def run_gui():
    root = tk.Tk()
    root.title("文本分析器")

    def analyze():
        word = simpledialog.askstring("输入", "请输入要分析的词或字:")
        if word:
            try:
                freq = count_frequency(full_text, use_word=len(word) > 1)[word]
                result_text.delete('1.0', tk.END)
                result_text.insert(tk.END, f"'{word}' 的频率是: {freq}\n")
            except Exception as e:
                messagebox.showerror("错误", str(e))

    tk.Button(root, text="分析", command=analyze).pack()
    result_text = tk.Text(root, height=4, width=50)
    result_text.pack()

    def open_analysis():
        main_analysis("dreamofredmaison.txt", ['之', '其', '也', '者', '于', '而'])
        plot_frequency()

    tk.Button(root, text="打开全文分析", command=open_analysis).pack()

    root.mainloop()


if __name__ == "__main__":
    run_gui()
