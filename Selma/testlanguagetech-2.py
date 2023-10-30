# -*- coding: utf-8 -*-
# %pylab inline
import regex as re
import math
import string
from collections import Counter
# from __future__ import division


"""
Created on Thu Sep 16 23:23:43 2021

@author: 4stra
"""

text=open("gosta.txt","r",encoding=('utf-8')).read()

# text="this is a test this "

def tokens(text):
    return re.findall(r'\p{Ll}+', text)


tex=tokens(text)
con=Counter(tex)

most=con.most_common(2)

print(sum(con.values()))

def pdist (counterr):
    N=sum(list(counterr.values()))
    return lambda x:counterr[x]/N

p=pdist(con)




