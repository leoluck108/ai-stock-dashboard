import streamlit as st
import akshare as ak
import pandas as pd

st.set_page_config(page_title="A股交易仪表盘", layout="wide")

@st.cache_data(ttl=600)
def get_data():
    try:
        return ak.stock_board_industry_name_em()
    except:
        return pd.DataFrame()

def calc(df):
    if df.empty:
        return df
    df = df.copy()
    df["涨跌幅"] = pd.to_numeric(df["涨跌幅"], errors="coerce")
    df["强度"] = df["涨跌幅"]
    return df

st.title("📊 A股AI交易仪表盘")

df = get_data()
df = calc(df)

if df.empty:
    st.error("数据获取失败，请刷新")
else:
    st.metric("市场状态", "运行正常")
    st.dataframe(df.sort_values("强度", ascending=False))