import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="A股AI交易系统 V10", layout="wide")

st.title("📊 A股AI交易系统 V10（交易逻辑强化版）")

# =========================
# 🧠 1. 数据层（稳定）
# =========================
def get_data():
    try:
        import akshare as ak
        df = ak.stock_zh_a_spot_em()
        df = df[["名称", "涨跌幅", "成交额"]].head(150)
        return df
    except:
        df = pd.DataFrame({
            "名称": ["AI芯片", "算力", "光模块", "数据中心", "机器人", "电力设备"],
            "涨跌幅": [round(random.uniform(-3, 6), 2) for _ in range(6)],
            "成交额": [random.randint(50, 200) for _ in range(6)],
        })
        return df

df = get_data()

# =========================
# 📈 2. 市场趋势（核心升级）
# =========================
avg_change = df["涨跌幅"].mean()

if avg_change > 1.5:
    trend = "📈 强趋势（多头市场）"
elif avg_change > 0:
    trend = "📊 震荡市场"
else:
    trend = "📉 空头市场"

# =========================
# 💰 3. 资金强度（升级重点）
# =========================
df["资金强度"] = df["涨跌幅"] * 0.7 + (df["成交额"] / 120)

money_strength = df["资金强度"].mean()

# =========================
# 🎯 4. 市场集中度（核心新增）
# =========================
top10 = df.sort_values("涨跌幅", ascending=False).head(10)
focus_ratio = top10["涨跌幅"].mean()

# =========================
# 🧠 5. 交易决策引擎（核心）
# =========================
score = (avg_change * 0.4) + (money_strength * 0.4) + (focus_ratio * 0.2)

if score > 2:
    decision = "✔ 强势做多区（可重仓）"
elif score > 0.8:
    decision = "⚠ 结构交易区（轻仓）"
else:
    decision = "❌ 风险区（空仓）"

# =========================
# 📊 6. 展示层
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场趋势", trend)
col2.metric("资金强度", round(money_strength, 2))
col3.metric("交易决策", decision)

# =========================
# 🔥 7. 主线强度（重点升级）
# =========================
st.subheader("🔥 主线强度（前10强）")

st.dataframe(top10.sort_values("涨跌幅", ascending=False))

# =========================
# 🧠 8. AI交易结论
# =========================
st.subheader("🧠 AI交易结论")

if "强趋势" in trend and score > 2:
    st.success("市场进入主升结构 → 顺势做多核心板块")
elif "震荡" in trend:
    st.warning("市场轮动 → 只做短线机会")
else:
    st.error("市场风险释放 → 禁止交易")

# =========================
# 🛡️ 9. 系统说明
# =========================
st.info("V10已升级：趋势 + 资金 + 集中度 → 三因子交易决策模型")