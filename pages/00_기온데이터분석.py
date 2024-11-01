import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일에서 데이터를 불러오기
data = pd.read_csv("daily_temp.csv")


# 일교차 열 생성하기
df['일교차'] = df['최고기온'] - df['최저기온']
pd.to_datetime(df['날짜'])
df['날짜'] = pd.to_datetime(df['날짜'])

df['년'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day
df['요일'] = df['날짜'].dt.weekday
df


def season (t) : 
    if t>20 :
        return '여름'
    elif t<5 :
        return '겨울'
    else :
        return '봄/가을'

df['계절'] = df['평균기온'].apply(season)

import matplotlib.pyplot as plt
import koreanize_matplotlib
