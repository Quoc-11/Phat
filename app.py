import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Công Cụ Tính Lãi Gửi Tiết Kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Công Cụ Tính Lãi Gửi Tiết Kiệm")
st.write("Nhập thông tin khoản tiền gửi của bạn để tính toán tiền lãi dự kiến.")

st.divider()

# --- NHẬP THÔNG TIN ---
col1, col2 = st.columns(2)

with col1:
    so_tien_gui = st.number_input(
        "Số tiền gửi (VNĐ):",
        min_value=1_000_000,
        value=100_000_000,
        step=1_000_000,
        format="%d"
    )
    st.caption(f"👉 **{so_tien_gui:,.0f} VNĐ**")

    ky_han = st.number_input(
        "Kỳ hạn gửi (tháng):",
        min_value=1,
        max_value=60,
        value=12,
        step=1
    )

with col2:
    lai_suat = st.number_input(
        "Lãi suất (%/năm):",
        min_value=0.1,
        max_value=20.0,
        value=6.0,
        step=0.1,
        format="%.2f"
    )

    hinh_thuc = st.selectbox(
        "Hình thức nhận lãi:",
        options=["Lãi cuối kỳ", "Lãi hàng tháng", "Lãi hàng quý"]
    )

st.divider()

# --- TÍNH TOÁN LÃI SUẤT ---
# Tổng tiền lãi cho toàn bộ kỳ hạn (Công thức chuẩn ngân hàng: Lãi năm / 12 * số tháng)
tong_lai = so_tien_gui * (lai_suat / 100) * (ky_han / 12)

# Tính lãi định kỳ theo hình thức nhận
if hinh_thuc == "Lãi cuối kỳ":
    lai_dinh_ky = tong_lai
    ten_dinh_ky = "Tiền lãi nhận vào cuối kỳ"
elif hinh_thuc == "Lãi hàng tháng":
    lai_dinh_ky = tong_lai / ky_han
    ten_dinh_ky = "Tiền lãi nhận hàng tháng"
else:  # Lãi hàng quý
    # Mỗi quý có 3 tháng
    so_quy = ky_han / 3
    lai_dinh_ky = tong_lai / so_quy if so_quy >= 1 else tong_lai
    ten_dinh_ky = "Tiền lãi nhận hàng quý"

tong_goc_va_lai = so_tien_gui + tong_lai

# --- HIỂN THỊ KẾT QUẢ ---
st.subheader("📊 Kết quả tính toán")

m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    st.metric(
        label=ten_dinh_ky,
        value=f"{lai_dinh_ky:,.0f} VNĐ"
    )

with m_col2:
    st.metric(
        label="Tổng tiền lãi thu được",
        value=f"{tong_lai:,.0f} VNĐ"
    )

with m_col3:
    st.metric(
        label="Tổng gốc + lãi cuối kỳ",
        value=f"{tong_goc_va_lai:,.0f} VNĐ"
    )

# Bảng tóm tắt thông tin
st.markdown("### 📝 Tóm tắt khoản gửi")
st.table({
    "Thông tin": ["Số tiền gửi ban đầu", "Kỳ hạn", "Lãi suất áp dụng", "Hình thức nhận lãi", "Tổng tiền thực nhận"],
    "Giá trị": [
        f"{so_tien_gui:,.0f} VNĐ",
        f"{ky_han} tháng",
        f"{lai_suat:.2f}% / năm",
        hinh_thuc,
        f"{tong_goc_va_lai:,.0f} VNĐ"
    ]
})
