import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

main=pd.read_csv("メインファイル")　#空欄がある行を削除済み

main_values_df=main.loc[:,["SEN_01_MA",
"SEN_02_MA",
"SEN_03_MA",
"SEN_04_MA",
"SEN_05_MA",
"SEN_06_MA",
"SEN_07_MA",
"SEN_08_MA",
"SEN_09_MA",
"SEN_10_MA",
"SEN_11_MA",
"SEN_12_MA",
"SEN_13_MA",
"SEN_14_MA",
"SEN_15_MA",
"SEN_16_MA",
"SEN_17_MA",
"SEN_18_MA",
"SEN_19_MA",
"SEN_20_MA",
"SEN_21_MA",
"SEN_22_MA",
"SEN_23_MA",
"SEN_24_MA",
"SEN_25_MA",
"SEN_26_MA",
"SEN_27_MA",
"SEN_28_MA",
"SEN_29_MA",
"SEN_30_MA",
"SEN_31_MA",
"SEN_32_MA",
"SEN_33_MA"]]

main_values_np=np.array(main_values)
main_values_np=main_values_np.astype(np.int)

# クラスターの数は６
pred=KMeans(n_clusters=6).fit_predict(main_values_np)

# 所属するクラスター名を表示する列を追加
main_values_df['cluster_id']=pred

# 各クラスターに何人いるか
main_values_df['cluster_id'].value_counts()

# クラスター１における各消費価値観項目の平均値
main_values_df[main_values_df['cluster_id']==1].mean()

# 平均値をクラスターごとにまとめたデータフレームを作成
cluster_info = pd.DataFrame()
for i in range(6):
    mean=main_values_df[main_values_df['cluster_id']==i].mean()
    mean=np.array(mean)
    cluster_info['cluster' + str(i)] =  mean

# 保存
cluster_info.to_excel('cluster_all_6.xlsx')
