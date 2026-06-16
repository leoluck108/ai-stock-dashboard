import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="A股AI交易仪表盘V2", layout="wide")

st.title("📊 A股AI交易系统 V2（升级版）")

# =========================
# 1️⃣ 模拟板块数据（后面可换真实数据）
# =========================
data = {
    "板块": ["AI芯片", "算力", "光模块", "数据中心", "机器人", "电力AI"],
    "涨跌幅": [3.2, 2.1, -0.5, 1.8, 4.5, 0.6],
    "成交热度": [80, 70, 40, 60, 90, 50]
}

df = pd.DataFrame(data)

# =========================
# 2️⃣ 计算“强度评分”
# =========================
df["强度评分"] = df["涨跌幅"] * 0.7 + df["成交热度"] * 0.3

# =========================
# 3️⃣ 市场状态判断
# =========================
avg_strength = df["强度评分"].mean()

if avg_strength > 60:
    market_state = "🔥 主升行情（积极做多）"
    signal = "✔ 可重仓"
elif avg_strength > 40:
    market_state = "🟡 震荡行情（控制仓位）"
    signal = "⚠ 轻仓参与"
else:
    market_state = "🔴 退潮行情（空仓为主）"
    signal = "❌ 禁止交易"

# =========================
# 4️⃣ 展示核心指标
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场状态", market_state)
col2.metric("交易信号", signal)
col3.metric("平均强度", round(avg_strength, 2))

# =========================
# 5️⃣ 板块排名
# =========================
st.subheader("📊 板块强度排行")

df_sorted = df.sort_values("强度评分", ascending=False)

st.dataframe(df_sorted)

# =========================
# 6️⃣ 结论区
# =========================
st.subheader("🧠 AI结论")

if avg_strength > 60:
    st.success("当前市场处于资金推动阶段，可围绕AI核心板块操作")
elif avg_strength > 40:
    st.warning("市场轮动明显，只能做短线")
else:
    st.error("市场风险较高，建议降低交易频率")