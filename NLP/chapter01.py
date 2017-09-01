# -*- coding:utf-8 -*-
"""
用途，文档说明
"""
from nltk.book import *

def lexical_diversity(text):
    # 词汇
    return len(text)/len(set(text))

def percentage(count,tatal):
    return 100*count/tatal
