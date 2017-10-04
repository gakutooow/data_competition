import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# アクセスログからANAのwebページへのアクセスだけを記したファイル（ana_log.txt）の作成
f = open("ana_log.txt","w")
for line in open("アクセスログデータ"):
    if "www.ana.co.jp" in line:
        f.write(line)
        count+=1
f.close()

df = pd.DataFrame(index=[], columns=["アドレス","個人ID","日付","時間","URL"])
array = np.array([])
count=0
for line in open("ana_log.txt","r"):
    words = line.split()
    series = Series(words,index=["アドレス","個人ID","日付","時間","URL"])
    df = df.append(series, ignore_index=True)

# ファイルに余計なwebページへのアクセス情報が含まれたのでドロップさせる
for i in range(len(df)):
    if df.ix[i,"アドレス"] != "www.ana.co.jp":
        df=df.drop(i)

df.to_excel("ana_df.xlsx")
