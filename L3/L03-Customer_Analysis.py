import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 读取原始CSV文件数据
    data = pd.read_csv('L03-Mall_Customers.csv', encoding='gbk')
    # print(data)
    # 选取原始数据中需要分析的数据字段
    analysis_data = data[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    # print(analysis_data)

    # 对性别标签进行标准化,Male为1，Female为0
    # print(analysis_data['Gender'])
    le = preprocessing.LabelEncoder()
    # le = le.fit(['Male', 'Female'])
    # print(le)
    analysis_data['Gender'] = le.fit_transform(analysis_data['Gender'])
    # print(analysis_data)

    # 对标签做归一化处理
    min_max_scaler = preprocessing.MinMaxScaler()
    analysis_data = min_max_scaler.fit_transform(analysis_data)
    # print(analysis_data)

    # 使用手肘法来分析k值=4，
    sse = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(analysis_data)
        sse.append(kmeans.inertia_)
    x = range(1, 10)
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.plot(x, sse, 'o-')
    plt.savefig('L03-plt_shouzhoufa.jpg')
    plt.show()

    # 使用KMeans做聚类分析
    kmeans = KMeans(n_clusters=4)
    # kmeans.fit(analysis_data)
    predict_k = kmeans.fit_predict(analysis_data)
    # print(predict_k)

    # 将聚类结果写入到数据最后一列
    result = pd.concat((data, pd.DataFrame(predict_k)), axis=1)
    # print(result)
    # 重命名聚类结果列的字段名
    result.rename({0: 'KMeans结果'}, axis=1, inplace=True)
    print(result)
    # 保存结果数据到csv文件
    result.to_csv("L03-customer_analysis_result.csv", index=False)



