import streamlit as st
import pandas as pd

st.set_page_config(page_title="A股AI仪表盘", layout="wide")

st.title("📊 A股AI交易仪表盘（稳定版）")

data = {
    "板块": ["AI芯片", "算力", "光模块", "数据中心"],
    "涨跌幅": [3.2, 2.1, -0.5, 1.8]
}

df = pd.DataFrame(data)

st.success("数据加载成功（模拟数据）")

st.dataframe(df)