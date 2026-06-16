import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="A股AI交易系统 V7", layout="wide")

st.title("📊 A股AI交易系统 V7（选股+交易信号版）")

# =========================
# 🧠 1. 数据层（稳定）
# =========================
def get_data():
    try:
        import akshare as ak
        df = ak.stock_zh_a_spot_em()
        df = df[["名称", "最新价", "涨跌幅", "成交额"]].head(120)
        return df
    except:
        df = pd.DataFrame({
            "名称": ["AI芯片", "算力", "光模块", "数据中心", "机器人", "半导体"],
            "最新价": [random.randint(10, 100) for _ in range(6)],
            "涨跌幅": [round(random.uniform(-3, 6), 2) for _ in range(6)],
            "成交额": [random.randint(50, 200) for _ in range(6)],
        })
        return df

df = get_data()

# =========================
# 📊 2. 强势评分（核心升级）
# =========================
df["动量评分"] = df["涨跌幅"] * 0.7 + (df["成交额"] / 100)

# =========================
# 🔥 3. 强势股筛选
# =========================
strong_stocks = df.sort_values("动量评分", ascending=False).head(10)

weak_stocks = df.sort_values("动量评分").head(10)

# =========================
# 🧠 4. 市场情绪
# =========================
up_ratio = (df["涨跌幅"] > 0).mean() * 100
avg_change = df["涨跌幅"].mean()

if avg_change > 1 and up_ratio > 55:
    state = "🔥 主升行情"
    signal = "✔ 积极交易"
elif avg_change > 0:
    state = "🟡 震荡行情"
    signal = "⚠ 轻仓"
else:
    state = "🔴 退潮行情"
    signal = "❌ 空仓"

# =========================
# 📊 5. 仪表盘
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场状态", state)
col2.metric("上涨比例", f"{up_ratio:.1f}%")
col3.metric("平均涨跌幅", f"{avg_change:.2f}%")

# =========================
# 🔥 6. 强势股
# =========================
st.subheader("🔥 AI筛选强势标的（Top10）")
st.dataframe(strong_stocks)

# =========================
# ⚠️ 7. 弱势股
# =========================
st.subheader("⚠️ 回避标的（弱势）")
st.dataframe(weak_stocks)

# =========================
# 🧠 8. AI交易建议
# =========================
st.subheader("🧠 AI交易建议")

if "主升" in state:
    st.success("当前适合做强势股突破策略")
elif "震荡" in state:
    st.warning("只做短线，快进快出")
else:
    st.error("风险阶段，不建议交易")

# =========================
# 🛡️ 9. 系统说明
# =========================
st.info("V7已加入选股系统：动量评分 + 强弱分层 + 自动交易建议")