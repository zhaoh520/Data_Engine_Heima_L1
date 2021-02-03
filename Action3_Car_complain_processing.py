#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#原始数据读取
data = pd.read_csv(r"C:\Users\zhaohong3\Desktop\L1\car_data_analyze\car_complain.csv", encoding='utf-8')
print(data)

#拆分Problem列
data2 = data.join(data['problem'].str.split(',', expand=True))
print(data2)


#按照厂家及车型分类计数
result = data2.groupby(['brand', 'car_model'], as_index=False)['desc'].count()
print(result)


#按照厂家分类计数并降序排列
result1 = data2.groupby('brand', as_index=False)['desc'].count()
print(result1.sort_values('desc', ascending=False))


#车型分类计数并降序排列
result2 = data2.groupby('car_model', as_index=False)['desc'].count()
print(result2.sort_values('desc', ascending=False))

