import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.simpledialog

# 创建应用程序窗口
app = tkinter.Tk()
app.title('My Notepad----by Dong Fuguo')
app['width'] = 800
app['height'] = 600

# 标记当前内容是否发生过改变，是否需要保存
textChanged = tkinter.IntVar(app, value=0)

# 当前文件名
filename = ''

# 创建菜单
menu = tkinter.Menu(app)
# File子菜单
# tearoff=0表示该子菜单不可以独立
# tearoff=1时，子菜单顶端会有一个虚线
submenu = tkinter.Menu(menu, tearoff=0)
def Open():
    global filename
    # 如果内容已改变，先保存
    if textChanged.get():
        yesno = tkinter.messagebox.askyesno(title='Save or not?',
                                            message='Do you want to save?')
        if yesno == tkinter.YES:
            Save()
    
    filename = tkinter.filedialog.askopenfilename(title='Open file',
                                                  filetypes=[('Text files', '*.txt')])
    if filename:
        # 清空内容,0.0是lineNumber.Column的表示方法
        txtContent.delete(0.0, tkinter.END)
        with open(filename, 'r', encoding='utf8') as fp:
            txtContent.insert(tkinter.INSERT, ''.join(fp.readlines()))
        # 标记为尚无修改
        textChanged.set(0)
# 创建Open菜单并绑定菜单时间处理函数
submenu.add_command(label='Open', command=Open)

def Save():
    global filename
    # 如果是第一次保存新建文件，则打开“另存为”窗口
    if not filename:
        SaveAs()
    # 如果内容发生改变，保存
    elif textChanged.get():
        with open(filename, 'w') as fp:
            fp.write(txtContent.get(0.0, tkinter.END))
        textChanged.set(0)
submenu.add_command(label='Save', command=Save)

def SaveAs():
    global filename
    # 打开“另存为”窗口
    newfilename = tkinter.filedialog.asksaveasfilename(title='Save As',
                                                       initialdir=r'c:\\',
                                                       initialfile='new.txt')
    #如果指定了文件名，则保存文件
    if newfilename:
        with open(newfilename, 'w') as fp:
            fp.write(txtContent.get(0.0, tkinter.END))
        filename = newfilename
        textChanged.set(0)
submenu.add_command(label='Save As', command=SaveAs)

#添加分割线
submenu.add_separator()

def Close():
    global filename
    Save()
    txtContent.delete(0.0, tkinter.END)
    # 置空文件名
    filename = ''
submenu.add_command(label='Close', command=Close)
# 将子菜单关联到主菜单上
menu.add_cascade(label='File', menu=submenu)

# Edit子菜单
submenu = tkinter.Menu(menu, tearoff=0)

# 撤销最后一次操作
def Undo():
    # 启用undo标志
    txtContent['undo'] = True
    try:
        txtContent.edit_undo()
    except Exception as e:
        pass
submenu.add_command(label='Undo', command=Undo)

def Redo():
    txtContent['undo'] = True
    try:
        txtContent.edit_redo()
    except Exception as e:
        pass
submenu.add_command(label='Redo', command=Redo)

# 添加分割线
submenu.add_separator()

def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())
submenu.add_command(label='Copy', command=Copy)

def Cut():
    Copy()
    # 删除所选内容
    txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
submenu.add_command(label='Cut', command=Cut)

def Paste():
    # 如果没有选中内容，则直接粘贴到鼠标位置
    # 如果有所选内容，则先删除再粘贴
    try:
        txtContent.insert(tkinter.SEL_FIRST, txtContent.clipboard_get())
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        # 如果粘贴成功就结束本函数，以免异常处理结构执行完成之后再次粘贴
        return
    except Exception as e:
        pass
    txtContent.insert(tkinter.INSERT, txtContent.clipboard_get())    
submenu.add_command(label='Paste', command=Paste)

submenu.add_separator()

def Search():
    # 获取要查找的内容
    textToSearch = tkinter.simpledialog.askstring(title='Search',
                                                  prompt='What to search?')
    start = txtContent.search(textToSearch, 0.0, tkinter.END)

    if start:
        tkinter.messagebox.showinfo(title='Found', message='Ok')
    else:
        tkinter.messagebox.showerror(title='Not Found', message='Fail')
submenu.add_command(label='Search', command=Search)

menu.add_cascade(label='Edit', menu=submenu)

# Help菜单
submenu = tkinter.Menu(menu, tearoff=0)
def About():
    tkinter.messagebox.showinfo(title='About',
                                message='作者：董付国\n微信公众号：Python小屋')        
submenu.add_command(label='About', command=About)
menu.add_cascade(label='Help', menu=submenu)

# 将创建的菜单关联到应用程序窗口
app.config(menu=menu)

# 创建文本编辑组件
txtContent = tkinter.scrolledtext.ScrolledText(app, wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH, expand=tkinter.YES)
def KeyPress(event):
    textChanged.set(1)
txtContent.bind('<KeyPress>', KeyPress)

app.mainloop()
