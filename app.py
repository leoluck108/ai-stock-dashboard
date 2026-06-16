import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="A股AI交易系统 V8", layout="wide")

st.title("📊 A股AI交易系统 V8（交易决策系统）")

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
            "涨跌幅": [round(random.uniform(-3, 6), 2) for _ in range(6)],
            "成交额": [random.randint(50, 200) for _ in range(6)],
        })
        return df

df = get_data()

# =========================
# 📊 2. 市场结构判断（核心升级）
# =========================
up_ratio = (df["涨跌幅"] > 0).mean() * 100
avg_change = df["涨跌幅"].mean()

if avg_change > 1.5 and up_ratio > 60:
    structure = "📈 上升结构"
    trade_state = "✔ 重仓区"
elif avg_change > 0:
    structure = "📊 震荡结构"
    trade_state = "⚠ 轻仓区"
else:
    structure = "📉 下跌结构"
    trade_state = "❌ 禁止交易"

# =========================
# 🟡 3. 动量评分（升级版）
# =========================
df["动量"] = df["涨跌幅"] * 0.8 + (df["成交额"] / 120)

strong = df.sort_values("动量", ascending=False).head(10)

weak = df.sort_values("动量").head(10)

# =========================
# 🧾 4. 核心指标展示
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场结构", structure)
col2.metric("上涨比例", f"{up_ratio:.1f}%")
col3.metric("交易状态", trade_state)

# =========================
# 🔥 5. 强势机会
# =========================
st.subheader("🔥 主线机会（Top10）")
st.dataframe(strong)

# =========================
# ⚠️ 6. 风险标的
# =========================
st.subheader("⚠️ 回避标的")
st.dataframe(weak)

# =========================
# 🧠 7. 交易纪律（新增核心）
# =========================
st.subheader("🧠 AI交易纪律")

if "重仓区" in trade_state:
    st.success("市场结构健康，可围绕主线做趋势交易")
elif "轻仓" in trade_state:
    st.warning("市场分化，只做短线机会")
else:
    st.error("市场风险释放，禁止交易，等待结构修复")

# =========================
# 🛡️ 8. 系统说明
# =========================
st.info("V8已加入：市场结构判断 + 交易纪律系统 + 主线机会筛选")