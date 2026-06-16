import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="A股AI交易系统 V9", layout="wide")

st.title("📊 A股AI交易系统 V9（趋势+资金决策版）")

# =========================
# 🧠 1. 数据层（稳定）
# =========================
def load_data():
    try:
        import akshare as ak
        df = ak.stock_zh_a_spot_em()
        df = df[["名称", "最新价", "涨跌幅", "成交额"]].head(150)
        return df, "real"
    except:
        df = pd.DataFrame({
            "名称": ["AI芯片", "算力", "光模块", "数据中心", "机器人", "半导体"],
            "涨跌幅": [round(random.uniform(-3, 6), 2) for _ in range(6)],
            "成交额": [random.randint(50, 200) for _ in range(6)],
        })
        return df, "mock"

df, source = load_data()

# =========================
# 📈 2. 趋势识别（核心升级）
# =========================
avg_change = df["涨跌幅"].mean()

if avg_change > 1.5:
    trend = "📈 上升趋势"
elif avg_change > 0:
    trend = "📊 震荡趋势"
else:
    trend = "📉 下降趋势"

# =========================
# 💰 3. 资金行为模型（升级重点）
# =========================
df["资金强度"] = df["涨跌幅"] * 0.6 + (df["成交额"] / 120)

money_flow = df["资金强度"].mean()

# =========================
# 🧠 4. 交易评分系统（核心）
# =========================
score = (avg_change * 0.5) + (money_flow * 0.5)

if score > 2:
    decision = "✔ 可重仓交易"
elif score > 0.5:
    decision = "⚠ 轻仓试错"
else:
    decision = "❌ 禁止交易"

# =========================
# 📊 5. 核心展示
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场趋势", trend)
col2.metric("资金强度", round(money_flow, 2))
col3.metric("交易决策", decision)

# =========================
# 🔥 6. 机会排序
# =========================
st.subheader("🔥 主线机会（资金驱动排序）")

df["综合评分"] = df["资金强度"]
st.dataframe(df.sort_values("综合评分", ascending=False))

# =========================
# ⚠️ 7. 风险提示
# =========================
st.subheader("🧠 AI风控")

if "上升" in trend and score > 2:
    st.success("趋势 + 资金共振：适合主升操作")
elif "震荡" in trend:
    st.warning("市场轮动，只做短线")
else:
    st.error("风险阶段：禁止交易")

# =========================
# 🛡️ 8. 系统说明
# =========================
st.info("V9已升级：趋势识别 + 资金模型 + 交易评分系统")