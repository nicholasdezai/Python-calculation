import wave
import threading
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import pyaudio

CHUNK_SIZE = 1024
CHANNELS = 2
FORMAT = pyaudio.paInt16
RATE = 44100

fileName = None
allowRecording = False

def record():
    global fileName
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)

    wf = wave.open(fileName, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    while allowRecording:
        # 从录音设备读取数据，直接写入wav文件
        data = stream.read(CHUNK_SIZE)
        wf.writeframes(data)
    wf.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    fileName = None

# 创建tkinter应用程序
root = tkinter.Tk()
root.title('录音机--董付国')
root.geometry('280x80+400+300')
root.resizable(False, False)

# 开始按钮
def start():
    global allowRecording, fileName    
    fileName = tkinter.filedialog.asksaveasfilename(filetypes=[('未压缩波形文件',
                                                                '*.wav')])
    if not fileName:
        return
    if not fileName.endswith('.wav'):
        fileName = fileName+'.wav'
    allowRecording = True
    lbStatus['text'] = '正在录音...'
    threading.Thread(target=record).start()
btnStart = tkinter.Button(root, text='开始录音', command=start)
btnStart.place(x=30, y=20, width=100, height=20)

# 结束按钮
def stop():
    global allowRecording
    allowRecording = False
    lbStatus['text'] = '准备就绪'
btnStop = tkinter.Button(root, text='停止录音', command=stop)
btnStop.place(x=140, y=20, width=100, height=20)

lbStatus = tkinter.Label(root, text='准备就绪', anchor='w', fg='green')
lbStatus.place(x=30, y=50, width=200, height=20)

# 关闭程序时检查是否正在录制
def closeWindow():
    if allowRecording:
        tkinter.messagebox.showerror('正在录制', '请先停止录制')
        return
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)

root.mainloop()
