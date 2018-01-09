#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pyecharts import Bar

title='bar chart'
index=pd.date_range('3/2/2017',periods=6,freq='M')
df1=pd.DataFrame(np.random.randn(6),index=index)
df2=pd.DataFrame(np.random.randn(6),index=index)

dtvalue1=[i[0] for i in df1.values]
dtvalue2=[i[0] for i in df2.values]
_index=[i for i in df1.index.format()]

bar=Bar(title,'profit and loss situation')
bar.add('profit',_index,dtvalue1)
bar.add('loss',_index,dtvalue2)
bar.render()