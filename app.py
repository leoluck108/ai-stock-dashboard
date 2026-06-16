import streamlit as st
import akshare as ak
import pandas as pd
import numpy as np

# 页面标题
st.set_page_config(page_title="AI产业链交易仪表盘", layout="wide")

# 获取板块数据（自动更新）
@st.cache_data(ttl=600)
def 获取数据():
    return ak.stock_board_industry_name_em()

# 计算强度
def 计算强度(df):
    df = df.copy()
    df["涨跌幅"] = pd.to_numeric(df["涨跌幅"], errors="coerce")
    df["强度"] = df["涨跌幅"]
    return df

# 市场状态判断
def 市场状态(平均值):
    if 平均值 > 2:
        return "主升（可以做）"
    elif 平均值 > 0:
        return "轮动（小仓）"
    else:
        return "退潮（不做）"

# 标题
st.title("📊 A股AI产业链交易仪表盘（手机可用版）")

# 数据
df = 获取数据()
df = 计算强度(df)

# 状态
状态 = 市场状态(df["强度"].mean())

# 显示
st.metric("当前市场状态", 状态)

st.subheader("板块强度排序")
st.dataframe(df.sort_values("强度", ascending=False))

# 交易提示
if "主升" in 状态:
    st.success("✔ 可以交易（趋势明确）")
elif "轮动" in 状态:
    st.warning("⚠ 轻仓试错")
else:
    st.error("✖ 不建议交易")