from os import mkdir
from os.path import isdir
from re import findall, sub
from urllib.request import urlopen

#公众号“Python小屋”历史文章清单，可以用手机进入公众号，打开菜单“最新资源”==>“历史文章”
#然后复制链接，在使用电脑端浏览器打开该链接
startUrl = r'https://mp.weixin.qq.com/s/u9FeqoBaA3Mr0fPCUMbpqA'

#读取网页源代码，提取每篇文章的url
pattern = r'<p>.*?<a href="(.+?)" target="_blank".+?data-linktype="2">(.+?)</a>.*?</p>'
with urlopen(startUrl) as fp:
    content = fp.read().decode()
    
for perUrl, title in findall(pattern, content):
    #删除文章标题中可能的HTML代码
    title = sub('<.+?>', '', title)
    print('正在爬取文章：', title)
    with urlopen(perUrl) as fp:
        content = fp.read().decode()
    if not isdir(title):
        mkdir(title)
    #爬取网页中的图片地址
    pattern = r'<img .*? data-type="png".*?data-src="(.+?)"'
    for index, picUrl in enumerate(findall(pattern, content)):
        with open(title+'\\{}.png'.format(index), 'wb') as fpPic:
            fpPic.write(urlopen(picUrl).read())
