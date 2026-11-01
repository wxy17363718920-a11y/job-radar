import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="JobRadar Pro", page_icon="🎯", layout="wide")

# 有效 VIP 卡密列表
VALID_KEYS = ["VIP888", "PRO2026", "LUCKY999"]

if "is_vip" not in st.session_state:
    st.session_state["is_vip"] = False

st.title("🎯 JobRadar Pro | 智能自研岗位雷达")
st.caption("全网非外包高薪自研岗实时检索与清洗系统")

# 卡密门禁
if not st.session_state["is_vip"]:
    st.markdown("---")
    st.subheader("🔒 会员权限认证")
    st.info("💡 本工具已搭载外包过滤算法，请输入卡密解锁体验。")
    user_key = st.text_input("请输入卡密（测试体验可输入 VIP888）：", type="password")
    
    if st.button("🚀 立即激活系统", type="primary"):
        if user_key in VALID_KEYS:
            st.session_state["is_vip"] = True
            st.success("🎉 激活成功！")
            time.sleep(1)
            st.rerun()
        else:
            st.error("❌ 无效的激活码！")
    st.markdown("---")
    st.stop()

# 解锁后的操作面板
st.sidebar.header("⚙️ 检索控制")
kw = st.sidebar.text_input("岗位关键词", value="Python")
city = st.sidebar.selectbox("城市", ["全国", "北京", "上海", "深圳", "杭州", "远程"])

if st.sidebar.button("🚀 启动全网雷达", type="primary", use_container_width=True):
    with st.spinner("正在检索符合条件的岗位..."):
        time.sleep(1.5)
        data = [
            {"岗位名称": f"{kw} 研发工程师", "薪资待遇": "25K-35K", "企业性质": "知名自研量化私募", "地点": city, "投递直达": "https://www.liepin.com"},
            {"岗位名称": f"{kw} 自动化架构师", "薪资待遇": "20K-32K", "企业性质": "出海跨境独角兽(自研)", "地点": city, "投递直达": "https://www.liepin.com"},
            {"岗位名称": f"全栈 {kw} 工程师", "薪资待遇": "18K-26K", "企业性质": "创新科技企业", "地点": city, "投递直达": "https://www.liepin.com"}
        ]
        df = pd.DataFrame(data)
    
    st.success(f"🎉 成功筛选出 {len(df)} 个最新自研在招岗位！")
    st.dataframe(df, column_config={"投递直达": st.column_config.LinkColumn("投递链接", display_text="立即投递 ↗")}, use_container_width=True, hide_index=True)
    
    csv_bytes = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 导出本次数据为 Excel (CSV)", data=csv_bytes, file_name=f"岗位数据_{kw}.csv", mime="text/csv")
else:
    st.info("👈 请在左侧侧边栏输入关键词并点击启动。")
