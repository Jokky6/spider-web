import requests

from PIL import Image,ImageDraw
import numpy
import re
from fontTools.ttLib import TTFont

def get_url(html):
    try:
        regex=re.compile('href="(.*?/svgtextcss/.*?)">')
        baseurl=re.findall(regex,html)
        url='http:'+baseurl[0]
        return url
    except:
        print('html有问题')

def woff_download(file_name,file_dict):
    woff = 'http:'+file_dict[file_name]
    woff_response = requests.get(woff)
    with open('font.woff', 'wb') as f:
        f.write(woff_response.content)

def fontconvert(woff_name):
    global result
    codeDict = {}
    font = TTFont(woff_name)
    uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder()
    best_cmap = font['cmap'].getBestCmap()
    print(best_cmap)
    print(uni_list)

if __name__ =='__main__':
    # headers={
    #     "Host": "www.dianping.com",
    #     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    # }
    # response = requests.get('http://www.dianping.com/beijing/ch10/g110',headers=headers).text
    # svgtexturl = get_url(response)
    # woffRegex = re.compile('format\("embedded-opentype"\),url\("(.*?)"\)')  # 匹配woff文件url的正则表达式
    # woffurls = set(re.findall(woffRegex, requests.get(svgtexturl).text))
    # woffnames = re.findall('font/(.*?).woff', str(woffurls))  # 匹配woff文件名
    # woffnames = set([i + '.woff' for i in woffnames])
    # woffdict = dict(zip(woffnames, woffurls))
    fontconvert('font.woff')

