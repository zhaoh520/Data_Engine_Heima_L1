import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

# 读取原始数据
data = pd.read_csv('train.csv')
# print(data.head())
data['Datetime'] = pd.to_datetime(data['Datetime'], format="%d-%m-%Y %H:%M")
# print(data.dtypes)
# print(data.head())

# 取日期列及数据列
data['Date'] = data['Datetime'].dt.date
# print(data.head())
data_origin = data.loc[:, ['Date', 'Count']]
data_origin['Date'] = pd.to_datetime(data_origin['Date'], format='%Y-%m-%d')
# data_origin.to_csv('test.csv')
# print(data_origin)
# print(data_origin.dtypes)

# 按照日期计数
data_groupby_day = data_origin.groupby('Date').sum('Count').reset_index()
# print(data_groupby_day)
# print(data_groupby_day.columns)
data_groupby_day.rename(columns={'Date':'ds', 'Count':'y'}, inplace=True)
print(data_groupby_day.head())
# # 拟合模型
model = Prophet()
print(model.growth)
model.fit(data_groupby_day)

# 预测日期，未来7个月
future = model.make_future_dataframe(periods=210)

# 构建预测数据集
forecast = model.predict(future)

# 打印结果
print(forecast)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# 展示预测结果
model.plot(forecast)
plt.show()
plt.savefig('Train_forecast.png')
