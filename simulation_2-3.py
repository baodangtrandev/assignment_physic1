import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ==========================================
# 1. HẰNG SỐ VÀ GIÁ TRỊ KHỞI TẠO
# ==========================================
EPS_0 = 8.854e-12
V_INIT = 860        # V (Lấy theo thông số trên ảnh của bạn)
D_INIT = 30         # mm 
K_INIT = 2.0        # kappa

# ==========================================
# 2. THIẾT LẬP GIAO DIỆN CHÍNH
# ==========================================
# Chỉnh lại kích thước cửa sổ gọn gàng hơn
fig = plt.figure(figsize=(10, 8))
fig.canvas.manager.set_window_title('Khảo sát Năng lượng Tụ điện')
fig.suptitle('Đồ thị Khảo sát Mật độ Năng lượng Điện trường', fontsize=16, fontweight='bold')

# Vùng chứa đồ thị 2D (Được mở rộng ra giữa màn hình)
ax2d = fig.add_axes([0.15, 0.35, 0.75, 0.5])

# Chỗ trống hiển thị Text (Chỉ số)
text_ax = fig.add_axes([0.15, 0.9, 0.75, 0.05])
text_ax.axis('off')
info_text = text_ax.text(0.5, 0.5, '', transform=text_ax.transAxes, 
                         ha='center', va='center', fontsize=12, 
                         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

# ==========================================
# 3. HÀM VẼ ĐỒ THỊ 2D
# ==========================================
d_range = np.linspace(1, 50, 200)

def draw_2d_plot(ax, V, d_mm, k):
    ax.clear()
    
    # Tính toán
    E_arr = V / (d_range / 1000.0)
    uE_0 = 0.5 * 1.0 * EPS_0 * (E_arr**2)
    uE_k = 0.5 * k * EPS_0 * (E_arr**2)
    
    # Vẽ 2 đường cong
    ax.plot(d_range, uE_0, color='gray', linestyle='--', linewidth=2.5, label='Chân không ($\kappa=1$)')
    ax.plot(d_range, uE_k, color='royalblue', linewidth=2.5, label=f'Có điện môi ($\kappa={k:.1f}$)')
    
    # Vẽ thanh dọc (Vertical line) báo vị trí d hiện tại
    ax.axvline(d_mm, color='red', linestyle=':', linewidth=2, label=f'd = {d_mm} mm')
    
    ax.set_yscale('log')
    ax.set_title('So sánh Mật độ năng lượng ($u_E$) theo khoảng cách d', fontsize=13)
    ax.set_xlabel('Khoảng cách d (mm)', fontsize=11)
    ax.set_ylabel('u_E (J/m³) - Thang Log', fontsize=11)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)

# ==========================================
# 4. KHAI BÁO CÁC THANH TRƯỢT (SLIDERS)
# ==========================================
# Kéo dài các thanh trượt cho cân đối với đồ thị mới
ax_v = fig.add_axes([0.15, 0.2, 0.75, 0.03])
ax_d = fig.add_axes([0.15, 0.15, 0.75, 0.03])
ax_k = fig.add_axes([0.15, 0.1, 0.75, 0.03])

slider_v = Slider(ax_v, 'Hiệu điện thế V', 0, 1000, valinit=V_INIT, valstep=10)
slider_d = Slider(ax_d, 'Khoảng cách d (mm)', 1, 50, valinit=D_INIT, valstep=1)
slider_k = Slider(ax_k, 'Hằng số điện môi $\kappa$', 1.0, 10.0, valinit=K_INIT, valstep=0.1)

# ==========================================
# 5. HÀM CẬP NHẬT KHI KÉO THANH TRƯỢT
# ==========================================
def update(val):
    V_val = slider_v.val
    d_val = slider_d.val
    k_val = slider_k.val
    
    d_m = d_val / 1000.0
    E = V_val / d_m if d_m > 0 else 0
    uE_0 = 0.5 * 1.0 * EPS_0 * (E**2)
    uE_k = 0.5 * k_val * EPS_0 * (E**2)
    
    # Cập nhật Text
    text_str = (f"CƯỜNG ĐỘ E: {E:.2e} V/m   |   "
                f"u_E (Chân không): {uE_0:.2e} J/m³   |   "
                f"u_E (Điện môi): {uE_k:.2e} J/m³")
    info_text.set_text(text_str)
    
    # Chỉ gọi hàm cập nhật đồ thị 2D
    draw_2d_plot(ax2d, V_val, d_val, k_val)
    
    fig.canvas.draw_idle()

# Gắn sự kiện
slider_v.on_changed(update)
slider_d.on_changed(update)
slider_k.on_changed(update)

# Chạy lần đầu
update(None)

plt.show()