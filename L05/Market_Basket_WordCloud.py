import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import imageio

# 数据加载
data = pd.read_csv("./Market_Basket_Optimisation.csv", header=None)
# print(data)
# 整理数据，转换成transaction
transaction = list()
# 遍历原始数据集，并将其添加到transaction list中
for i in range(0, data.shape[0]):
    for j in range(0, data.shape[1]):
        # 判断是否为空，不为空则添加到list中
        if str(data.values[i, j]) != 'nan':
            transaction.append(data.values[i, j])
# print(transaction)

# 统计transaction中的各商品个数
item_count = pd.value_counts(transaction, ascending=False)
# print(type(item_count))
# 输出数量前10的商品
print(item_count[0:10])

# 将列表中的每一个元素用空格连接成一个字符串
transaction = " ".join(transaction)
# 导入词云背景图片
image_backgroud = imageio.imread('mineral_water.jpg')
# 设置词云图的大小、字体等参数
w = WordCloud(width=1000,
              height=700,
              # max_words=50,
              background_color='white',
              mask=image_backgroud,
              font_path='msyh.ttc')

# 生成词云
w.generate(transaction)
w.to_file('Market_Basket.png')
# 显示词云文件
plt.imshow(w)
plt.axis("off")
plt.show()



