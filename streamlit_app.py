import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("진주시 CCTV 위치 지도")

# 서버에 이미 파일이 있다고 가정
csv_file = "경상남도 진주시_CCTV위치정보_20250501.csv"

# 파일 읽기
try:
    df = pd.read_csv(csv_file, encoding="cp949")
except UnicodeDecodeError:
    df = pd.read_csv(csv_file, encoding="utf-8")

st.write("CCTV 데이터 미리보기", df.head())

# 지도 기준점(진주시청 근처)
center_lat, center_lon = 35.1802, 128.1076
m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

# CCTV 위치 마커 추가
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=f"목적: {row['목적']}<br>장소: {row['설치장소']}<br>대수: {row['설치대수']}",
        icon=folium.Icon(color='red', icon='camera')
    ).add_to(m)

# folium 지도 표시
st_folium(m, width=700, height=500)
