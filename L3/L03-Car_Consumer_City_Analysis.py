import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 读取原始CSV文件数据
    data = pd.read_csv('L03-car_data.csv', encoding='gbk')
    print(data)
    # 选取原始数据中需要分析的数据字段
    analysis_data = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]
    # print(analysis_data)
    # 采用scikit-learn 提供的层级聚类算法模型，每一个类簇的方差最小化，簇族分组量取4
    method = AgglomerativeClustering(linkage='ward', n_clusters=4)
    result = method.fit_predict(analysis_data)
    print(result)
    # 可视化层次聚类结果
    linkage_matrix = ward(analysis_data)
    dendrogram(linkage_matrix)
    plt.savefig('L03-plt_dendrogram.jpg')
    plt.show()
    # 将聚类结果添加到数据中
    result = pd.concat((data, pd.DataFrame(result)), axis=1)
    print(result)
    # 重命名聚类结果列的字段名
    result.rename({0: '层次聚类结果'}, axis=1, inplace=True)
    print(result)
    # 保存结果数据到csv文件
    result.to_csv("L03-Car_Customer_City_Analysis_result.csv", index=False)
