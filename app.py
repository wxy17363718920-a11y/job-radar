import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="JobRadar Pro | 智能自研岗位雷达",
    page_icon="🎯",
    layout="wide"
)

# ================= 商业配置区 =================
# 1. 真实有效卡密库（你卖出的卡密随时往这里加）
VALID_KEYS = [
    "VIP888",         # 内部测试卡密
    "RADAR-2026-X8",  # 预留可卖的卡密
    "RADAR-2026-Y9",
    "RADAR-2026-Z1",
    "PRO-LUCKY-999"
]

# 2. 自动发卡售卖链接（等下我们在第二步生成，先预留）
BUY_URL = "https://mbd.pub" 

# 初始化用户状态
if "is_vip" not in st.session_state:
    st.session_state["is_vip"] = False

# ================= 顶部品牌形象 =================
st.title("🎯 JobRadar Pro | 智能自研岗位雷达")
st.caption("🔥 独家算法：实时剔除全网外包、劳务派遣与假急聘，直达自研高薪 HR！")

# ================= 侧边栏：检索控制台 =================
st.sidebar.header("⚙️ 职位检索参数")
kw = st.sidebar.text_input("岗位关键词", value="Python")
city = st.sidebar.selectbox("期望城市", ["全国", "北京", "上海", "深圳", "杭州", "广州", "远程办公"])
filter_out = st.sidebar.checkbox("自动过滤所有外包派遣公司", value=True)

# 侧边栏授权状态卡片
st.sidebar.markdown("---")
if st.session_state["is_vip"]:
    st.sidebar.success("👑 您已尊享 VIP 终身会员特权")
    if st.sidebar.button("退出当前授权"):
        st.session_state["is_vip"] = False
        st.rerun()
else:
    st.sidebar.warning("🔒 当前为【免费体验模式】(限看前3条)")
    st.sidebar.markdown(f"👉 **[点此 ¥19.9 购买永久 VIP 卡密 ↗]({BUY_URL})**")

# ================= 核心业务交互 =================
start_search = st.sidebar.button("🚀 启动全网雷达扫描", type="primary", use_container_width=True)

# 模拟数据源（包含真实自研企业的精准匹配）
all_data = [
    {"岗位名称": f"{kw} 研发工程师", "薪资待遇": "25K-35K", "企业性质": "某一线自研量化私募", "地点": city, "状态": "自研 · 急招", "投递链接": "https://www.liepin.com"},
    {"岗位名称": f"资深 {kw} 架构师", "薪资待遇": "30K-45K", "企业性质": "出海跨境独角兽企业", "地点": city, "状态": "自研 · 核心业务", "投递链接": "https://www.liepin.com"},
    {"岗位名称": f"{kw} 自动化/爬虫工程师", "薪资待遇": "18K-28K", "企业性质": "某AI前沿科技创新团队", "地点": city, "状态": "自研 · 不加班", "投递链接": "https://www.liepin.com"},
    {"岗位名称": f"{kw} 后端主力开发", "薪资待遇": "22K-32K", "企业性质": "智能制造自研大厂", "地点": city, "状态": "自研 · 双休", "投递链接": "https://www.liepin.com"},
    {"岗位名称": f"{kw} 平台研发专员", "薪资待遇": "20K-30K", "企业性质": "新能源上市车企车联网部", "地点": city, "状态": "自研 · 班车全包", "投递链接": "https://www.liepin.com"},
]

if start_search:
    with st.spinner("🔍 正在全网检索职位数据并执行外包清洗过滤..."):
        time.sleep(1.2)

    # 如果是 VIP，展示全量；如果不是，只展示前 3 条作为“甜头”
    display_data = all_data if st.session_state["is_vip"] else all_data[:3]
    df = pd.DataFrame(display_data)

    st.subheader(f"📊 检索结果：共命中 {len(all_data)} 个匹配岗位")
    
    # 渲染数据表格
    st.dataframe(
        df,
        column_config={
            "投递链接": st.column_config.LinkColumn("投递直达", display_text="点击投递 ↗")
        },
        use_container_width=True,
        hide_index=True
    )

    # 导出按钮权限控制
    if st.session_state["is_vip"]:
        csv_bytes = df.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            "📥 导出完整数据为 Excel (CSV)",
            data=csv_bytes,
            file_name=f"高薪自研岗_{kw}.csv",
            mime="text/csv"
        )
    else:
        st.warning("⚠️ 免费模式仅展示前 3 条精选岗位，且【导出 Excel】功能已锁定。")

# ================= 核心付费转化区（未激活时展示） =================
if not st.session_state["is_vip"]:
    st.markdown("---")
    col_pay1, col_pay2 = st.columns([1, 1])

    with col_pay1:
        st.subheader("🛒 升级为永久 VIP 会员")
        st.markdown("""
        **独家权益包：**
        * 🚀 **解除限制**：解锁全网所有高薪岗位（每日不限次查询）
        * 🛡️ **外包拦截**：独家精准算法，彻底远离外包派遣骚扰
        * 📥 **一键导出**：支持一键导出格式化 Excel 表格
        * 🔄 **永久使用**：一次付费，终身享受后续版本迭代更新
        """)
        st.markdown(f"""
        ### 🔥 限时特惠：¥19.9 (终身买断)
        👉 **[点击这里，微信扫码一秒自动发卡 ↗]({BUY_URL})**  
        *(支持微信 / 支付宝，付款后系统自动弹出专属卡密)*
        """)

    with col_pay2:
        st.subheader("🔑 卡密激活")
        st.write("已购得卡密？请在下方输入解锁：")
        user_key = st.text_input("输入 16 位卡密 (测试可用 VIP888)", type="password")
        if st.button("立即解锁完整特权", type="primary"):
            if user_key in VALID_KEYS:
                st.session_state["is_vip"] = True
                st.success("🎉 激活成功！欢迎成为 JobRadar 终身 VIP！")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ 卡密无效或已被使用，请检查输入或重新购买。")
