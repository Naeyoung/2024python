import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# CSV 파일에서 데이터를 불러오기
data = pd.read_csv("daily_temp.csv")

# 특정 지역의 일교차를 계산하는 함수
def calculate_daily_temperature_range(data, location):
    location_data = data[data['location'] == location]
    location_data['temp_range'] = location_data['max_temp'] - location_data['min_temp']
    return location_data[['date', 'location', 'max_temp', 'min_temp', 'temp_range']]
