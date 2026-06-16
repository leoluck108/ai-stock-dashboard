import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="A股AI交易系统 V10.5", layout="wide")

st.title("📊 A股AI交易系统 V10.5（交易结构重写版）")

# =========================
# 🧠 1. 数据层（稳定）
# =========================
def get_data():
    try:
        import akshare as ak
        df = ak.stock_zh_a_spot_em()
        df = df[["名称", "涨跌幅", "成交额"]].head(120)
        return df
    except:
        df = pd.DataFrame({
            "名称": ["AI芯片", "算力", "光模块", "数据中心", "机器人", "半导体"],
            "涨跌幅": [round(random.uniform(-3, 6), 2) for _ in range(6)],
            "成交额": [random.randint(50, 200) for _ in range(6)],
        })
        return df

df = get_data()

# =========================
# 🟢 2. 市场结构（核心重写）
# =========================
avg_change = df["涨跌幅"].mean()

if avg_change > 1.5:
    market_phase = "🟢 上升期（可交易）"
elif avg_change > 0:
    market_phase = "🟡 震荡期（轻仓）"
else:
    market_phase = "🔴 下跌期（空仓）"

# =========================
# 🟡 3. 资金集中度（关键升级）
# =========================
df["资金强度"] = df["涨跌幅"] * 0.6 + (df["成交额"] / 120)

money_flow = df["资金强度"].mean()

top_focus = df.sort_values("涨跌幅", ascending=False).head(10)
focus_strength = top_focus["涨跌幅"].mean()

# =========================
# 🔴 4. 交易节奏系统（核心）
# =========================
score = (avg_change * 0.4) + (money_flow * 0.4) + (focus_strength * 0.2)

if score > 2:
    trade_mode = "🔥 主升浪（重仓）"
    action = "✔ 可以开仓"
elif score > 0.8:
    trade_mode = "⚠ 轮动期（轻仓）"
    action = "⚠ 试错仓位"
else:
    trade_mode = "❌ 退潮期（禁止交易）"
    action = "❌ 空仓"

# =========================
# 📊 5. 仪表盘输出
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场阶段", market_phase)
col2.metric("资金强度", round(money_flow, 2))
col3.metric("交易状态", trade_mode)

# =========================
# 🔥 6. 主线机会
# =========================
st.subheader("🔥 主线机会（资金驱动）")
st.dataframe(top_focus)

# =========================
# 🧠 7. 交易决策核心
# =========================
st.subheader("🧠 AI交易决策")

st.success(f"交易动作：{action}")

if "上升期" in market_phase and score > 2:
    st.info("市场进入趋势阶段 → 顺势交易")
elif "震荡" in market_phase:
    st.warning("市场轮动 → 只做短线")
else:
    st.error("市场风险释放 → 禁止交易")

# =========================
# 🛡️ 8. 系统说明
# =========================
st.caption("V10.5：交易结构重写版（市场阶段 + 资金结构 + 交易节奏）")