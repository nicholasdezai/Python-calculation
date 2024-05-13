from os import mkdir
from os.path import isdir
import datetime
from time import sleep
from threading import Thread
import cv2

#参数0表示笔记本自带摄像头
cap = cv2.VideoCapture(0)
#获取当前日期时间，例如2019-05-24 23:11:00
now = str(datetime.datetime.now())[:19].replace(':', '_')
dirName = now[:10]
tempAviFile = dirName+'\\'+now+'.avi'
if not isdir(dirName):
    mkdir(dirName)

#创建视频文件
aviFile = cv2.VideoWriter(tempAviFile,
                          cv2.VideoWriter_fourcc(*'MJPG'),
                          25, (640,480))  #帧速和视频宽度、高度

def write():
    while cap.isOpened():
        #捕捉当前图像，ret=True表示成功，False表示失败
        ret, frame = cap.read()
        if ret:
            #写入视频文件
            aviFile.write(frame)
    aviFile.release()
Thread(target=write).start()

input('按任意键结束.')
cap.release()
