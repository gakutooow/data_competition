import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import re
# 特定のwebページへのアクセスログだけを記したエクセルファイルを作成
class Log:
    def make_corp_log(self,corp_name):
        # 特定の企業のログだけ収集
        f = open("{}_log.txt".format(corp_name),"w")

        for line in open("../Webアクセスログ（20170128-20170228）.txt"):
            pattern = r"www\.jal\.co\.jp"
            matchOB = re.match(pattern , line)
            if matchOB and "jpg" not in line and "jpeg" not in line and "png" not in line and "gif" not in line :
                if  "css" not in line and "js" not in line and "ico" not in line and "xml" not in line and "tmpl" not in line:
                    f.write(line)


        for line in open("../Webアクセスログ（20170301-20170401）.txt"):
            pattern = r"www\.jal\.co\.jp"
            matchOB = re.match(pattern , line)
            if matchOB and "jpg" not in line and "jpeg" not in line and "png" not in line and "gif" not in line :
                if  "css" not in line and "js" not in line and "ico" not in line and "xml" not in line and "tmpl" not in line:
                    f.write(line)

        f.close()

        # ログをデータフレームとして管理
        df = pd.DataFrame(index=[], columns=["アドレス","個人ID","日付","時間","URL"])
        count=0
        for line in open("{}_log.txt".format(corp_name),"r"):
            words = line.split()
            series = Series(words,index=["アドレス","個人ID","日付","時間","URL"])
            df = df.append(series, ignore_index=True)
            count+=1
            if count % 1000 ==0:
                print("3_{}".format(count))

        # # ファイルに余計なwebページへのアクセス情報が含まれたのでドロップさせる
        # count=0
        # for i in range(len(df)):
        #     if df.ix[i,"アドレス"] != "www.jtb.co.jp":
        #         df=df.drop(i)
        #     count+=1
        #     if count % 1000 ==0:
        #         print("4_{}".format(count))

        df.to_excel("{}_df.xlsx".format(corp_name))

a=Log()
a.make_corp_log("jal")
