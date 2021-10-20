#csvファイルの読み込み
#ファイル形式
# "day","job","Ptime","starttime","endtime", "kokyaku", "kokyaku_total", "WD"

import pandas as pd
import numpy as np
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import datetime
data = ['E_JSCRMHKX01_', 'E_JSCRMWDX02_', 'E_JSSHGWDX04_', 'E_JSCRMHKX02_', 'E_JSCRMWDX01_']
#name = "E_JSCRMWDX03"
#name = "E_JSCRMWDX12_"
all_col_name = ['Ptime', 'kokyaku', 'kokyaku_total','WD', 'core']
for name in data:
    df = pd.read_csv('./csv/'+name+'.csv',header=0)
    # 標準化
    scaler = StandardScaler()
    scaler.fit(np.array(df))
    df_std = scaler.transform(np.array(df))
    df_std = pd.DataFrame(df_std,columns=df.columns)
    # 目的変数(Y)
    Y = np.array(df['Ptime'])
    Y_std = np.array(df_std['Ptime'])
    # 説明変数(X)
    col_name = ['kokyaku', 'kokyaku_total','WD', 'core']
    X = np.array(df[col_name])
    X_std = np.array(df_std[col_name])

    # データの分割(訓練データとテストデータ)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    Xs_train, Xs_test, Ys_train, Ys_test = train_test_split(X_std, Y_std, test_size=0.3, random_state=0)

    # モデル構築
    model = LinearRegression()
    model_std = LinearRegression()
    # 学習
    model.fit(X_train, Y_train)
    model_std.fit(Xs_train, Ys_train)
    # 回帰係数
    coef = pd.DataFrame({"col_name":np.array(col_name),"coefficient":model.coef_}).sort_values(by='coefficient')
    coef_std = pd.DataFrame({"col_name":np.array(col_name),"coefficient":model_std.coef_}).sort_values(by='coefficient')

    # 結果
    #coef.to_csv("out.csv")
    f = open('./output/output.csv',"a", newline='')
    writer = csv.writer(f)
    writer.writerow([name])
    writer.writerow(["【回帰係数】"])
    coef.to_csv(f)
    writer.writerow(["【標準化回帰係数】"])
    coef_std.to_csv(f)
    writer.writerow(["【切片】:", model.intercept_])
    writer.writerow(["【決定係数(訓練)】:", model.score(X_train, Y_train)])
    writer.writerow(["【決定係数(テスト)】:", model.score(X_test, Y_test)])
    f.close()
    #f.close()
    #writer.writerows(print("【切片】:", model.intercept_))
    #f.close()
    #print("【回帰係数】", coef)
    #print("【切片】:", model.intercept_)
    #print("【決定係数(訓練)】:", model.score(X_train, Y_train))
    #print("【決定係数(テスト)】:", model.score(X_test, Y_test))
    #print("【標準化回帰係数】", coef_std)
    graph = sns.pairplot(df[all_col_name])
    graph.savefig('./output/df_'+name+'Plot.png')
    graph_std = sns.pairplot(df_std[all_col_name])
    graph_std.savefig('./output/df_std_'+name+'Plot.png')
    #plt.show()