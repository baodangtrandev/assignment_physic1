import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ==========================================
# 1. HẰNG SỐ VÀ GIÁ TRỊ KHỞI TẠO
# ==========================================
EPS_0 = 8.854e-12
S = 0.04            # Diện tích bề mặt bản tụ (m^2)
V_INIT = 860        # V 
D_INIT = 30         # mm 
K_INIT = 2.0        # kappa

# ==========================================
# 2. THIẾT LẬP GIAO DIỆN CHÍNH
# ==========================================
fig = plt.figure(figsize=(10, 8))
fig.canvas.manager.set_window_title('Khảo sát năng lượng tụ điện')
fig.suptitle('Đồ thị khảo sát tổng năng lượng điện trường (W)', fontsize=16, fontweight='bold')

# Vùng chứa đồ thị 2D
ax2d = fig.add_axes([0.15, 0.35, 0.75, 0.5])

# Chỗ trống hiển thị Text (Chỉ số)
text_ax = fig.add_axes([0.15, 0.9, 0.75, 0.05])
text_ax.axis('off')
info_text = text_ax.text(0.5, 0.5, '', transform=text_ax.transAxes, 
                         ha='center', va='center', fontsize=12, 
                         bbox=dict(facecolor='white', alpha=0.9, edgecolor='forestgreen'))

# ==========================================
# 3. HÀM VẼ ĐỒ THỊ 2D
# ==========================================
d_range = np.linspace(1, 50, 200) # Khảo sát d từ 1mm đến 50mm

def draw_2d_plot(ax, V, d_mm, k):
    ax.clear()
    
    # Đổi mm sang mét
    d_m_range = d_range / 1000.0
    
    # Tính toán Tổng năng lượng (W đã được đổi đơn vị cực nhỏ sang Micro-Joules uJ cho số chẵn đẹp)
    W_0 = 0.5 * (1.0 * EPS_0 * S / d_m_range) * (V**2) * 1e6
    W_k = 0.5 * (k * EPS_0 * S / d_m_range) * (V**2) * 1e6
    
    # Vẽ 2 đường cong
    ax.plot(d_range, W_0, color='gray', linestyle='--', linewidth=2.5, label='Chân không ($\kappa=1$)')
    ax.plot(d_range, W_k, color='forestgreen', linewidth=2.5, label=f'Có điện môi ($\kappa={k:.1f}$)')
    
    # Vẽ thanh dọc (Vertical line) báo vị trí d hiện tại đang set trong Slider
    ax.axvline(d_mm, color='red', linestyle=':', linewidth=2, label=f'd = {d_mm} mm')
    
    ax.set_yscale('log')
    ax.set_title('So sánh tổng năng lượng (W) theo khoảng cách d', fontsize=13)
    ax.set_xlabel('Khoảng cách d (mm)', fontsize=11)
    ax.set_ylabel(r'Tổng năng lượng W ($\mu J$) - Thang Log', fontsize=11)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)

# ==========================================
# 4. KHAI BÁO CÁC THANH TRƯỢT (SLIDERS)
# ==========================================
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
    
    # Tính toán thông số Text ở thời điểm hiện tại
    d_m = d_val / 1000.0
    if d_m > 0:
        E = V_val / d_m
        W_0 = 0.5 * (1.0 * EPS_0 * S / d_m) * (V_val**2) * 1e6
        W_k = 0.5 * (k_val * EPS_0 * S / d_m) * (V_val**2) * 1e6
    else:
        E = 0
        W_0 = W_k = 0
    
    # Cập nhật Textbox (chữ r đằng trước để Python biểu diễn chuỗi Raw string chứa Text Math \mu)
    text_str = (f"Cường độ E: {E:.2e} V/m   |   "
                rf"W (Chân không): {W_0:.2f} $\mu J$   |   "
                rf"W (Điện môi): {W_k:.2f} $\mu J$")
    info_text.set_text(text_str)
    
    # Vẽ lại đồ thị
    draw_2d_plot(ax2d, V_val, d_val, k_val)
    
    fig.canvas.draw_idle()

# Gắn sự kiện (Event Listener)
slider_v.on_changed(update)
slider_d.on_changed(update)
slider_k.on_changed(update)

# Chạy cập nhật lần đầu tiên
update(None)

plt.show()
