import pandas as pd
import pystan
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("docomo.csv")

x=data.ix[:,["one","cm","mgz","paper"]]
y=data["change"]
z=data.ix[:,["one","SEX_CD","AGE","INCOM_SA"]]


stan_data = {'N': 2543, 'D':4,'E':4, 'x': x, 'y': y,'z':z}

fit = pystan.stan(file='docomo3.stan', data=stan_data, iter=100, chains=1)
print(fit)
print('Sampling finished.')

# 可視化
fit.plot()
plt.show()
