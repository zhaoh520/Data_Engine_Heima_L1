#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = {'chinese': [68, 95, 98, 90, 80], 'math': [65, 76, 86, 88, 90], 'english': [30, 98, 88, 77, 90]}
df = DataFrame(data, index=['Zhangfei', 'Guanyu', 'Liubei', 'Dianwei', 'Xuchu'], columns=['chinese', 'math', 'english'])
print(df)

# 成绩的平均值，方差等的统计结果输出
print(df.describe())

# 每个人各科成绩的总分及平均值
chengji = df[['chinese', 'math', 'english']]
print(chengji)
df['total'] = chengji.sum(axis=1)
df['average'] = chengji.mean(axis=1)
print(df)

# 按照每个人各科成绩的总分排序
print(df.sort_values('total', ascending=False))

