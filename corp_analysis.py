#  特定の企業のアクセスログデータを用いて、分析
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

class Analysis:
    def __init__(self,corp_name):
        self.df=pd.read_excel("{}_df.xlsx".format(corp_name))

    def drop(self,corp_name):
        # URLにjpg png gifなどを含むものを削除
        for i in range(len(self.df)):
            # self.dfのエクセルファイルの１列目を削除
            url = self.df.ix[i,4]
            if "jpg" in str(url):
                self.df=self.df.drop(i)
            elif "jpeg" in str(url):
                self.df=self.df.drop(i)
            elif "png" in str(url):
                self.df=self.df.drop(i)
            elif "gif" in str(url):
                self.df=self.df.drop(i)
            elif "css" in str(url):
                self.df=self.df.drop(i)
            elif "js" in str(url):
                self.df=self.df.drop(i)
            elif "ico" in str(url):
                self.df=self.df.drop(i)
            elif "xml" in str(url):
                self.df=self.df.drop(i)
            elif "tmpl" in str(url):
                self.df=self.df.drop(i)

        self.df.to_excel("{}_access_log.xlsx".format(corp_name))

    def number_of_access(self,corp_name):
        # 日にちごとのアクセス数
        number_of_access_per_day = self.df["日付"].value_counts()

        series=Series(number_of_access_per_day)
        print(series.head(20))

        # 日付順にソート
        series_sort=series.sort_index()
        series_sort.plot()
        plt.show()

a=Analysis('jal')
a.drop("jal")
a.number_of_access("jal")
