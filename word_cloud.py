# -*- coding: utf-8 -*-
"""
@Author         :  Guan Xiangqing
@Version        :  
@Company        :  Hunan qidian chuangzhi data technology co. LTD
@File           :  word_cloud.py
@Description    :  
@CreateTime     :  2020/6/10 0010 19:52
@ModifyTime     :  
"""

from os import path
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.font_manager import *
from wordcloud import WordCloud


def import_stopword(filename=''):
    """
    功能说明：加载停用词
    :param filename: 文件名字
    :return:
    """
    stopwords = {}
    f = open(filename, 'r', encoding='utf-8')
    line = f.readline()

    while line:
        stopwords.setdefault(line, 0)
        stopwords[line] = 1
        line = f.readline()
    f.close()
    return stopwords


def main():
    # 指定显示的字体
    font = os.path.join(os.path.dirname(__file__), u"../font/simhei.ttf")
    d = path.dirname(__file__)
    # mask = np.array(Image.open(path.join(d, "../image/stormtrooper_mask.png")))
    # 指定显示的背景图片
    mask = np.array(Image.open(path.join(d, "image/love.jpg")))
    # 指定文本
    text = open(u"data22.csv",encoding='UTF-8').read()
    # 指定停用词
    stopwords = import_stopword(filename='data/stopwords.txt')
    # 调用词云函数
    wc = WordCloud(font_path=font, max_words=2000, mask=mask, stopwords=stopwords, margin=10,
                   random_state=1).generate(text)

    # 指定默认字体
    # matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    # matplotlib.rcParams['font.family'] = 'sans-serif'
    # # 解决负号'-'显示为方块的问题
    # matplotlib.rcParams['axes.unicode_minus'] = False

    default_colors = wc.to_array()
    plt.imshow(default_colors)
    plt.title(u"novels' title & novelists'name  (Colour Picture)")
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__=='__main__':
    main()

