import streamlit as st
import akshare as ak
import pandas as pd

st.set_page_config(page_title="A股AI交易系统 V3", layout="wide")

st.title("📊 A股AI交易系统 V3（真实数据版）")

# =========================
# 1️⃣ 获取真实A股数据
# =========================
@st.cache_data(ttl=300)
def get_data():
    df = ak.stock_zh_a_spot_em()
    return df

df = get_data()

# =========================
# 2️⃣ 数据清洗
# =========================
df = df[["名称", "最新价", "涨跌幅", "成交额"]]
df["涨跌幅"] = pd.to_numeric(df["涨跌幅"], errors="coerce")
df["成交额"] = pd.to_numeric(df["成交额"], errors="coerce")

# =========================
# 3️⃣ 市场情绪计算
# =========================
up_ratio = (df["涨跌幅"] > 0).mean() * 100
avg_change = df["涨跌幅"].mean()

# =========================
# 4️⃣ 市场状态判断
# =========================
if avg_change > 1 and up_ratio > 55:
    state = "🔥 主升行情"
    signal = "✔ 重仓"
elif avg_change > 0:
    state = "🟡 震荡行情"
    signal = "⚠ 控仓"
else:
    state = "🔴 退潮行情"
    signal = "❌ 空仓"

# =========================
# 5️⃣ 展示核心指标
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场状态", state)
col2.metric("上涨比例", f"{up_ratio:.2f}%")
col3.metric("平均涨跌幅", f"{avg_change:.2f}%")

# =========================
# 6️⃣ 板块排名（简化版）
# =========================
st.subheader("📊 个股强度排行（前50）")

df_sorted = df.sort_values("涨跌幅", ascending=False).head(50)

st.dataframe(df_sorted)

# =========================
# 7️⃣ AI结论
# =========================
st.subheader("🧠 AI交易判断")

if "主升" in state:
    st.success("当前市场强势，可围绕AI与主线板块操作")
elif "震荡" in state:
    st.warning("市场分化，只做短线")
else:
    st.error("市场风险较高，建议空仓或轻仓")