import streamlit as st
import akshare as ak
import pandas as pd

st.set_page_config(page_title="A股AI仪表盘", layout="wide")

@st.cache_data(ttl=600)
def get_data():
    try:
        df = ak.stock_zh_a_spot_em()
        return df
    except:
        return pd.DataFrame()

st.title("📊 A股AI交易仪表盘")

df = get_data()

if df.empty:
    st.error("数据源暂时不可用（网络限制），点击刷新")
else:
    st.success("数据加载成功")
    st.dataframe(df.head(50))