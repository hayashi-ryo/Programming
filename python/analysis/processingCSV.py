#csvファイルを読み込み適切な形に加工する
#input
#ファイル形式
#day","job","Ptime","starttime","endtime"
#output
#"day","job","Ptime","starttime","endtime", "kokyaku", "kokyaku_total", "WD"

import pandas as pd
import datetime as dt
# kokyakuの追記
# kokyaku_totalの追記
# WDの追記
df['WD'] = pd.to_datetime(df['day']).dt.dayofweek