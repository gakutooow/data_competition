import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from scipy import stats
# レッドブル：PI_02_750707
# キリン一番搾り：PI_01_752603
# Twitter：CGM_F_02_MX
# インスタ：CGM_F_04_MX
main_csv = pd.read_csv("メインデータ,low_memory=False)
# 必要な列だけ取り出す
main = main_csv.loc[:,["SampleID","CGM_F_02_MX","CGM_F_04_MX","PI_01_752603","PI_02_750707"]]
# 列名を変更
main = main.rename(columns={"CGM_F_02_MX":"Twitter","CGM_F_04_MX":"instagram","PI_01_752603":"キリン","PI_02_750707":"レッドブル"})

# クロス集計データを作る
for i in range(len(main["SampleID"])):
    value = 1
    for m in range(4):
        for k in range(4):
            if main.ix[i,3] == "{}".format(k+1) and main.ix[i,4] == "{}".format(m+1):
                main.ix[i,"value"] = value
            value += 1

print(main.head())
# クロス集計データ
cross = np.array(main["value"].value_counts().sort_index()).reshape((4,4))
print(cross)


squared,p,dof,ef = stats.chi2_contingency(cross)
print("検定統計量" + str(squared))
print("p値" + str(p))
print("自由度" + str(dof))
print("期待度数")
print(str(ef))
