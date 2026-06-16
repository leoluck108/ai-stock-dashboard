import streamlit as st
import pandas as pd

st.set_page_config(page_title="A股AI交易系统 V5", layout="wide")

st.title("📊 A股AI交易系统 V5（工业级稳定版）")

# =========================
# 🧠 1. 数据层（三级容错）
# =========================
def get_data():
    try:
        import akshare as ak
        df = ak.stock_zh_a_spot_em()
        df = df[["名称", "最新价", "涨跌幅", "成交额"]]
        df = df.head(100)
        return df, "真实数据"
    except:
        try:
            # 第二层备用
            df = pd.read_csv("https://example.com/fallback.csv")
            return df, "备用数据"
        except:
            # 第三层兜底
            df = pd.DataFrame({
                "名称": ["AI芯片", "算力", "光模块", "数据中心", "机器人"],
                "涨跌幅": [2.3, 1.5, -0.4, 1.2, 3.8],
                "成交额": [120, 98, 60, 80, 150]
            })
            return df, "模拟数据"

df, source = get_data()

# =========================
# 🟡 2. 数据处理
# =========================
df["涨跌幅"] = pd.to_numeric(df.get("涨跌幅", 0), errors="coerce")

# =========================
# 🔥 3. 情绪指标
# =========================
up_ratio = (df["涨跌幅"] > 0).mean() * 100
avg_change = df["涨跌幅"].mean()

# =========================
# 📊 4. 市场状态模型
# =========================
if avg_change > 1 and up_ratio > 55:
    state = "🔥 主升行情"
    signal = "✔ 重仓"
elif avg_change > 0:
    state = "🟡 震荡行情"
    signal = "⚠ 轻仓"
else:
    state = "🔴 退潮行情"
    signal = "❌ 空仓"

# =========================
# 🧾 5. 仪表盘输出
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("市场状态", state)
col2.metric("上涨比例", f"{up_ratio:.2f}%")
col3.metric("数据来源", source)

# =========================
# 📊 6. 排序展示
# =========================
st.subheader("📊 强势标的排序")

st.dataframe(df.sort_values("涨跌幅", ascending=False))

# =========================
# 🧠 7. AI结论
# =========================
st.subheader("🧠 AI交易决策")

if "主升" in state:
    st.success("市场进入趋势行情，可围绕AI主线操作")
elif "震荡" in state:
    st.warning("市场轮动阶段，只做短线")
else:
    st.error("风险期，建议空仓或降低仓位")

# =========================
# 🛡️ 8. 稳定性提示
# =========================
st.caption("V5已启用三层容错：真实数据 → 备用数据 → 模拟数据，保证永不白屏")