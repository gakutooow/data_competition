import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

main=pd.read_csv(メインファイル)　#空欄がある行を削除済み

main_hobby_df=main.loc[:,["HOB_01_MA",
"HOB_02_MA",
"HOB_03_MA",
"HOB_04_MA",
"HOB_05_MA",
"HOB_06_MA",
"HOB_07_MA",
"HOB_08_MA",
"HOB_09_MA",
"HOB_10_MA",
"HOB_11_MA",
"HOB_12_MA",
"HOB_13_MA",
"HOB_14_MA",
"HOB_15_MA",
"HOB_16_MA",
"HOB_17_MA",
"HOB_18_MA",
"HOB_19_MA",
"HOB_20_MA",
"HOB_21_MA",
"HOB_22_MA",
"HOB_23_MA",
"HOB_24_MA",
"HOB_25_MA",
"HOB_26_MA",
"HOB_27_MA",
"HOB_28_MA",
"HOB_29_MA",
"HOB_30_MA",
"HOB_31_MA",
"HOB_32_MA"]]

main_hobby_array=np.array(main_hobby)
main_hobby_array=main_hobby.astype(np.int)

# クラスターの数は５
pred=KMeans(n_clusters=5).fit_predict(main_hobby_array)

# 所属するクラスター名を表示する列を追加
main_hobby_df['cluster_id']=pred

# 各クラスターに何人いるか
main_hobby_df['cluster_id'].value_counts()

# クラスター１における各消費価値観項目の平均値
main_hobby_df[main_hobby_df['cluster_id']==0].mean()

# 平均値をクラスターごとにまとめたデータフレームを作成
cluster_info = pd.DataFrame()
for i in range(5):
    mean=main_hobby_df[main_hobby_df['cluster_id']==i].mean()
    mean=np.array(mean)
    cluster_info['cluster' + str(i)] =  mean

# 保存
cluster_info.to_excel('cluster_all_5_by_hobby.xlsx')
