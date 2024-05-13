from os import mkdir
from os.path import isdir
import datetime
from time import sleep
import cv2

while True:
    #参数0表示笔记本自带摄像头
    cap = cv2.VideoCapture(0)
    #获取当前日期时间，例如2019-05-24 23:11:00
    now = str(datetime.datetime.now())[:19].replace(':', '_')
    if not isdir(now[:10]):
        mkdir(now[:10])
    #捕捉当前图像，ret=True表示成功，False表示失败
    ret, frame = cap.read()
    if ret:
        #保存图像，以当前日期时间为文件名
        fn = now[:10]+'\\'+now+'.jpg'
        cv2.imwrite(fn, frame)
    cap.release()
    #每5秒钟捕捉一次图像
    sleep(5)
