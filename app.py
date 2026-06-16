import streamlit as st
import pandas as pd
import random

# =========================
# 🎨 页面基础设置（美化关键）
# =========================
st.set_page_config(
    page_title="A股AI交易系统 V10.5 Pro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# 🎨 顶部标题（更像交易软件）
# =========================
st.markdown("""
<style>
.big-title {
    font-size:34px;
    font-weight:bold;
    text-align:center;
    margin-bottom:10px;
}
.sub-title {
    text-align:center;
    color:gray;
    margin-bottom:30px;
}
.card {
    padding:15px;
    border-radius:12px;
    background-color:#111827;
    color:white;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">📊 A股AI交易系统 V10.5 Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">趋势 + 资金 + 交易决策系统</div>', unsafe_allow_html=True)

# =========================
# 🧠 数据层（稳定）
# =========================
def get_data():
    df = pd.DataFrame({
        "名称": ["AI芯片", "算力", "光模块", "数据中心", "机器人", "电力设备"],
        "涨跌幅": [round(random.uniform(-3, 6), 2) for _ in range(6)],
        "成交额": [random.randint(50, 200) for _ in range(6)],
    })
    return df

df = get_data()

# =========================
# 📈 逻辑层（不改你的系统）
# =========================
avg_change = df["涨跌幅"].mean()
money_strength = (df["涨跌幅"] * 0.6 + df["成交额"] / 120).mean()

if avg_change > 1.5:
    market = "🟢 上升期"
    signal = "✔ 可交易"
    color = "green"
elif avg_change > 0:
    market = "🟡 震荡期"
    signal = "⚠ 控仓"
    color = "orange"
else:
    market = "🔴 下跌期"
    signal = "❌ 空仓"
    color = "red"

# =========================
# 🎨 卡片仪表盘（核心升级）
# =========================
col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="card">
<h3>市场状态</h3>
<h2>{market}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card">
<h3>资金强度</h3>
<h2>{money_strength:.2f}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="card">
<h3>交易信号</h3>
<h2>{signal}</h2>
</div>
""", unsafe_allow_html=True)

# =========================
# 📊 数据区（美化表格）
# =========================
st.markdown("---")
st.subheader("🔥 强势板块观察")

df["综合评分"] = df["涨跌幅"] * 0.7 + df["成交额"] / 120
df = df.sort_values("综合评分", ascending=False)

st.dataframe(df, use_container_width=True)

# =========================
# 🧠 AI结论区（增强视觉）
# =========================
st.markdown("---")
st.subheader("🧠 AI交易结论")

if "上升" in market:
    st.success("当前市场结构健康，可参与趋势交易")
elif "震荡" in market:
    st.warning("市场轮动，只做短线")
else:
    st.error("风险市场，禁止交易")

# =========================
# 🛡️ 底部说明
# =========================
st.caption("V10.5 Pro：仅优化UI，不改变交易逻辑")