import tkinter as tk
from foo import *


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        show_bar = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
        l = tk.Label(self, bg='green', fg='yellow', font=('Arial', 12), width=20, textvariable=show_bar)
        l.pack()

        def print_selection():
            # del_rotateword_page()
            value = lb.get(lb.curselection())  # 获取当前选中的文本
            show_bar.set(value)  # 为label设置值
            switch = {
                "rotateword": rotateword_page,
                "avoid": avoid_page,
                "useonly": useonly_page,
                "useall": useall_page,
                "hasnoe": hasnoe_page,
                "isabecedarian": isabecedarian_page
            }
            switch[value]()

        # 第5步，创建一个按钮并放置，点击按钮调用print_selection函数
        b1 = tk.Button(self, text='print selection', width=15, height=2, command=print_selection)
        b1.pack()

        # 第7步，创建Listbox并为其添加内容
        select_box = tk.StringVar()
        select_box.set(("rotateword", "avoid", "useonly", "useall", "hasnoe", "isabecedarian"))
        # 创建Listbox
        lb = tk.Listbox(self, listvariable=select_box)  # 将var2的值赋给Listbox
        lb.pack()

        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        def rotateword_page():
            subwindow = tk.Toplevel(self)
            subwindow.title("rotateword_page")  # 设置子窗口的标题

            # 在子窗口中添加一个按钮，点击后可以关闭子窗口
            close_button = tk.Button(subwindow, text="关闭", command=subwindow.destroy)
            close_button.pack(side="bottom")
            # 为foo中rotateword函数设置ui
            rotateword_label = tk.Label(subwindow, text="rotateword:")
            rotateword_label.pack()
            rotateword_entry = tk.Entry(subwindow)
            rotateword_entry.pack()
            rotateword_n_label = tk.Label(subwindow, text="n:")
            rotateword_n_label.pack()
            rotateword_n_entry = tk.Entry(subwindow)
            rotateword_n_entry.pack()
            # 设计一个按钮，点击后调用rotateword函数，并在输入文本框中显示结果

            rotateword_framerotateword_button = tk.Button(subwindow, text="rotateword", command=
                lambda : var.set(rotateword(rotateword_entry.get(), int(rotateword_n_entry.get()))))
            rotateword_framerotateword_button.pack()

            var = tk.StringVar()
            l = tk.Label(subwindow, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
            l.pack()

        def avoid_page():
            subwindow = tk.Toplevel(self)
            subwindow.title("avoid_page")  # 设置子窗口的标题
            close_button = tk.Button(subwindow, text="关闭", command=subwindow.destroy)
            close_button.pack(side="bottom")

            avoid_label = tk.Label(subwindow, text="word:")
            avoid_label.pack()
            avoid_entry = tk.Entry(subwindow)
            avoid_entry.pack()
            avoid_list_label = tk.Label(subwindow, text="avoid list:")
            avoid_list_label.pack()
            avoid_list_entry = tk.Entry(subwindow)
            avoid_list_entry.pack()

            avoid_button = tk.Button(subwindow, text="avoid", command=
                lambda : var.set("True" if avoid_1(avoid_entry.get(), list(avoid_list_entry.get())) else "False"))
            avoid_button.pack()

            var = tk.StringVar()
            l = tk.Label(subwindow, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
            l.pack()

        def useonly_page():
            subwindow = tk.Toplevel(self)
            subwindow.title("useonly_page")
            close_button = tk.Button(subwindow, text="关闭", command=subwindow.destroy)
            close_button.pack(side="bottom")
            useonly_label = tk.Label(subwindow, text="word:")
            useonly_label.pack()
            useonly_entry = tk.Entry(subwindow)
            useonly_entry.pack()
            useonly_list_label = tk.Label(subwindow, text="useonly list:")
            useonly_list_label.pack()
            useonly_list_entry = tk.Entry(subwindow)
            useonly_list_entry.pack()
            useonly_button = tk.Button(subwindow, text="useonly", command=
                lambda : var.set("True" if useonly(useonly_entry.get(), list(useonly_list_entry.get())) else "False"))
            useonly_button.pack()
            var = tk.StringVar()
            l = tk.Label(subwindow, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
            l.pack()

        def useall_page():
            subwindow = tk.Toplevel(self)
            subwindow.title("useall_page")
            close_button = tk.Button(subwindow, text="关闭", command=subwindow.destroy)
            close_button.pack(side="bottom")
            useall_label = tk.Label(subwindow, text="word:")
            useall_label.pack()
            useall_entry = tk.Entry(subwindow)
            useall_entry.pack()
            useall_list_label = tk.Label(subwindow, text="useall list:")
            useall_list_label.pack()
            useall_list_entry = tk.Entry(subwindow)
            useall_list_entry.pack()
            useall_button = tk.Button(subwindow, text="useall", command=
            lambda: var.set("True" if useall(useall_entry.get(), list(useall_list_entry.get())) else "False"))

            useall_button.pack()
            var = tk.StringVar()
            l = tk.Label(subwindow, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
            l.pack()

        def hasnoe_page():
            subwindow = tk.Toplevel(self)
            subwindow.title("hasnoe_page")
            close_button = tk.Button(subwindow, text="关闭", command=subwindow.destroy)
            close_button.pack(side="bottom")
            hasnoe_label = tk.Label(subwindow, text="word:")
            hasnoe_label.pack()
            hasnoe_entry = tk.Entry(subwindow)
            hasnoe_entry.pack()
            hasnoe_button = tk.Button(subwindow, text="hasnoe",
                                      command=lambda: var.set("True" if hasnoe(hasnoe_entry.get()) else "False"))
            hasnoe_button.pack()
            var = tk.StringVar()
            l = tk.Label(subwindow, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
            l.pack()

        def isabecedarian_page():
            subwindow = tk.Toplevel(self)
            subwindow.title("isabecedarian_page")
            close_button = tk.Button(subwindow, text="关闭", command=subwindow.destroy)
            close_button.pack(side="bottom")
            isabecedarian_label = tk.Label(subwindow, text="word:")
            isabecedarian_label.pack()
            isabecedarian_entry = tk.Entry(subwindow)
            isabecedarian_entry.pack()
            isabecedarian_button = tk.Button(subwindow, text="isabecedarian",
                                             command=lambda: var.set(
                                                 "True" if isabecedarian(isabecedarian_entry.get()) else "False"))
            isabecedarian_button.pack()
            var = tk.StringVar()
            l = tk.Label(subwindow, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
            l.pack()


# 创建应用程序窗口实例
root = tk.Tk()
app = Application(master=root)
# 设置窗口标题
app.master.title('Hello Tkinter')
# 设置窗口大小
app.master.geometry('960x540')

# 主事件循环开始
app.mainloop()
