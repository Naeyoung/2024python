# pandas 라이브러리 불러오기

import pandas as pd
import streamlit as st
import plotly.express as px

# 판다스에서 csv 데이터 읽어오기
df = pd.read_csv('daily_temp.csv')

# 타이틀과 설명 추가
st.title('첫 프로젝트 일별 기온 분석')

st.write("전체 통계 자료 data summary📊")

df = df.rename(columns = {'평균기온(℃)': '평균기온', '최저기온(℃)': '최저기온','최고기온(℃)': '최고기온'})
df['일교차'] = df['최고기온']-df['최저기온']
# 전체 데이터 통계 요약 출력
st.write(df.describe())


# 날짜 데이터의 년, 월, 일, 요일 정보 추출
pd.to_datetime(df['날짜'])
df['날짜'] = pd.to_datetime(df['날짜'])
df['년'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day
df['요일'] = df['날짜'].dt.weekday

# 월 선택 옵션 추가 
selected_months = st.selectbox("평균 기온이 궁금한 달을 선택하세요", range(1,13), format_func=lambda x:f"{x}월"})

# 선택한 월의 데이터만 필터링
selected_month_data = df[df['월'] == selected_month]

#년도별 평균 기온 계산
selected_month_avg_temp = selected_month_data.groupby('년')['평균기온'].mean().reset_index() 

#그래프 출력
st.write("10월 평균기온 추이🤓")
fig = px.line(october_avg_temp, x='년', y='평균기온', title = '년도별 {selected_month}월 평균 기온 변화', labels ={'년':'년도', '평균기온':'평균기온'})
st.plotly_chart(fig)
