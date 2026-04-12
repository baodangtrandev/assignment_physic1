import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. HẰNG SỐ VÀ GIÁ TRỊ CỐ ĐỊNH 
# ==========================================
EPS_0 = 8.854e-12
S = 0.04       
V_def = 470    
d_def = 0.018  
k_def = 2.0    

# ==========================================
# 2. KHỞI TẠO KHUNG ĐỒ THỊ (FIX LỖI ĐÈ CHỮ)
# ==========================================
# Tăng chiều cao của cửa sổ lên một chút (từ 5.5 lên 6) để có thêm không gian
fig, axs = plt.subplots(1, 3, figsize=(16, 6))

# FIX 1: Đặt y=0.95 (nhỏ hơn 1) để tiêu đề nằm hoàn toàn bên trong cửa sổ đồ thị
fig.suptitle('Khảo sát sự phụ thuộc của tổng năng lượng ($W$)', 
             fontsize=18, fontweight='bold', y=0.95)

# FIX 2: Hạ top=0.80. Tức là 3 đồ thị con chỉ cao tới mức 80% của cửa sổ, 
# chừa hẳn 20% không gian trống phía trên đỉnh cho cái Tiêu đề chính.
plt.subplots_adjust(left=0.08, bottom=0.15, right=0.95, top=0.80, wspace=0.35)

# ==========================================
# 3. ĐỒ THỊ 1: W THEO HIỆU ĐIỆN THẾ V
# ==========================================
V_arr = np.linspace(0, 1000, 100)
W_v = 0.5 * (k_def * EPS_0 * S / d_def) * (V_arr**2)

axs[0].plot(V_arr, W_v * 1e6, color='purple', linewidth=2.5) 
axs[0].set_title(r'Phụ thuộc vào hiệu điện thế $V$', fontsize=13, pad=15)
axs[0].set_xlabel('Hiệu điện thế V (Volts)', fontsize=11)
axs[0].set_ylabel('Tổng năng lượng W ($\mu J$)', fontsize=11)
axs[0].grid(True, linestyle='--', alpha=0.6)

axs[0].text(100, max(W_v * 1e6) * 0.85, r'$W \propto V^2$', 
            fontsize=14, bbox=dict(facecolor='white', alpha=0.8, edgecolor='purple'))

# ==========================================
# 4. ĐỒ THỊ 2: W THEO KHOẢNG CÁCH d
# ==========================================
d_arr = np.linspace(0.005, 0.05, 100) 
W_d = 0.5 * (k_def * EPS_0 * S / d_arr) * (V_def**2)

axs[1].plot(d_arr * 1000, W_d * 1e6, color='green', linewidth=2.5)
axs[1].set_title(r'Phụ thuộc vào khoảng cách $d$', fontsize=13, pad=15)
axs[1].set_xlabel('Khoảng cách d (mm)', fontsize=11)
axs[1].set_ylabel('Tổng năng lượng W ($\mu J$)', fontsize=11)
axs[1].grid(True, linestyle='--', alpha=0.6)

axs[1].text(30, max(W_d * 1e6) * 0.85, r'$W \propto \frac{1}{d}$', 
            fontsize=14, bbox=dict(facecolor='white', alpha=0.8, edgecolor='green'))

# ==========================================
# 5. ĐỒ THỊ 3: W THEO HẰNG SỐ ĐIỆN MÔI epsilon
# ==========================================
k_arr = np.linspace(1, 10, 100)
W_k = 0.5 * (k_arr * EPS_0 * S / d_def) * (V_def**2)

axs[2].plot(k_arr, W_k * 1e6, color='darkorange', linewidth=2.5)
axs[2].set_title(r'Phụ thuộc vào hằng số điện môi $\epsilon$', fontsize=13, pad=15)
axs[2].set_xlabel(r'Hằng số điện môi $\epsilon$ (hoặc $\kappa$)', fontsize=11)
axs[2].set_ylabel('Tổng năng lượng W ($\mu J$)', fontsize=11)
axs[2].grid(True, linestyle='--', alpha=0.6)

axs[2].text(2, max(W_k * 1e6) * 0.85, r'$W \propto \epsilon$', 
            fontsize=14, bbox=dict(facecolor='white', alpha=0.8, edgecolor='darkorange'))

# Lưu ý: Lần này KHÔNG dùng plt.tight_layout() ở cuối nữa vì nó sẽ ghi đè 
# lên cái subplots_adjust mà chúng ta đã setup cực kỳ cẩn thận ở Bước 2.
plt.show()