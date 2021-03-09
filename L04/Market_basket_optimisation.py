import pandas as pd
import numpy as np
from efficient_apriori import apriori
from mlxtend.frequent_patterns import apriori as ap
from mlxtend.frequent_patterns import association_rules

# 1.获取原始数据
data = pd.read_csv("./Market_Basket_Optimisation.csv", header=None)
# print(data)
# data.shape = (7501, 20)
# print(data.shape)
# print(data.values[0,0])

# 2.整理数据，转换成transaction
transaction = list()
# 遍历原始数据集，并将其添加到transaction list中
for i in range(0,data.shape[0]):
    temp = list()
    for j in range(0, data.shape[1]):
        # 判断是否为空，不为空则添加到list中
        if str(data.values[i,j]) != 'nan':
            temp.append(data.values[i,j])
    transaction.append(temp)
# print(transaction)

# 3.使用efficient_apriori，设定关联规则的参数（support、confident）挖掘关联规则
itemsets, rule = apriori(transaction,min_support=0.02,min_confidence=0.4)
print("efficient_apriori频繁项集：",  itemsets)
print("efficient_apriori关联规则：", rule)

# 4.使用mlxtend.frequent_patterns方法
from mlxtend.preprocessing import TransactionEncoder
# 定义模型
te = TransactionEncoder()
# 传入模型的数据需要满足特定的格式，将其转换为bool值，
df_tf = te.fit_transform(transaction)
df = pd.DataFrame(df_tf,columns=te.columns_)
# print(df)
# 导入apriori方法，设置最小支持度min_support=0.02，求频繁项集
frequent_itemsets = ap(df,min_support=0.02,use_colnames=True)
# 频繁项集按支持度排序
frequent_itemsets.sort_values(by='support',ascending=False,inplace=True)
print("mlxtend.frequent_patterns频繁项集：", frequent_itemsets)

# metric可以有很多的度量选项，返回的表列名都可以作为参数
association_rule = association_rules(frequent_itemsets,metric='confidence',min_threshold=0.4)
# 关联规则按leverage排序
association_rule.sort_values(by='leverage',ascending=False,inplace=True)

print("mlxtend.frequent_patterns关联规则：", association_rule)


