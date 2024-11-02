# pandas 라이브러리 불러오기
import pandas as pd
# 판다스에서 csv 데이터 읽어오기
df = pd.read_csv('daily_temp.csv')

# 타이틀과 설명 추가
st.title('첫 프로젝트 일별 기온 분석')
st.write("년도별 일별 기온 분석하기📊")

df['일교차'] = df['최고기온']-df['최저기온']
