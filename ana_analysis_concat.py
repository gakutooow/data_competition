import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

# 読み込むエクセルファイルは１列目を削除済み
ana_df_1=pd.read_excel("ana_df_1.xlsx")
# URLにjpg png gifを含むものを削除
for i in range(len(ana_df_1)):
    url = ana_df_1.ix[i,4]
    if "jpg" in str(url):
        ana_df_1=ana_df_1.drop(i)
    elif "png" in str(url):
        ana_df_1=ana_df_1.drop(i)
    elif "gif" in str(url):
        ana_df_1=ana_df_1.drop(i)

# 読み込むエクセルファイルは１列目を削除済み
ana_df_2=pd.read_excel("ana_df_2.xlsx")
# URLにjpg png gifを含むものを削除
for i in range(len(ana_df_2)):
    url = ana_df_2.ix[i,4]
    if "jpg" in str(url):
        ana_df_2=ana_df_2.drop(i)
    elif "png" in str(url):
        ana_df_2=ana_df_2.drop(i)
    elif "gif" in str(url):
        ana_df_2=ana_df_2.drop(i)

# ２つのデータをまとめる
ana_df=pd.concat([ana_df_1,ana_df_2])
# 日にちごとのアクセス数
number_of_access_per_day = ana_df["日付"].value_counts()

series=Series(number_of_access_per_day)
print(series.head(20))

# 日付順にソート
series_sort=series.sort_index()
series_sort.plot()
print(series.head(20))
plt.show()
