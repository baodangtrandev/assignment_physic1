import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. HẰNG SỐ VÀ THAM SỐ CỐ ĐỊNH
# ==========================================
EPS_0 = 8.854e-12
S = 0.04          # Diện tích bản tụ (m^2)

# Các giá trị cố định khi khảo sát 1 biến
V_fixed = 500     # Hiệu điện thế 500V
d_fixed = 0.01    # Khoảng cách 10mm
kappa_fixed = 1.0 # Môi trường chân không

# ==========================================
# 2. KHỞI TẠO DỮ LIỆU
# ==========================================
V_arr = np.linspace(0, 1000, 200)       # 0 - 1000V
d_arr = np.linspace(0.01, 0.05, 200)    # 10mm - 50mm
kappa_arr = np.linspace(1, 10, 200)     # 1 - 10

# ==========================================
# 3. TÍNH TOÁN TỔNG NĂNG LƯỢNG (uJ)
# ==========================================
# Công thức: W = 0.5 * (kappa * EPS_0 * S / d) * V^2
W_V = 0.5 * (kappa_fixed * EPS_0 * S / d_fixed) * (V_arr**2) * 1e6
W_d = 0.5 * (kappa_fixed * EPS_0 * S / d_arr) * (V_fixed**2) * 1e6
W_kappa = 0.5 * (kappa_arr * EPS_0 * S / d_fixed) * (V_fixed**2) * 1e6

# ==========================================
# 4. VẼ ĐỒ THỊ 2D
# ==========================================
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# --- Đồ thị 1: W theo V ---
axs[0].plot(V_arr, W_V, color='blue', linewidth=2.5)
axs[0].set_title(r'$W$ phụ thuộc $V$ ($W \propto V^2$)', fontsize=14, pad=15)
axs[0].set_xlabel('Hiệu điện thế V (V)', fontsize=12)
axs[0].set_ylabel(r'Tổng năng lượng W ($\mu J$)', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].fill_between(V_arr, W_V, color='blue', alpha=0.1)

# --- Đồ thị 2: W theo d ---
axs[1].plot(d_arr, W_d, color='red', linewidth=2.5)
axs[1].set_title(r'$W$ phụ thuộc $d$ ($W \propto \frac{1}{d}$)', fontsize=14, pad=15)
axs[1].set_xlabel('Khoảng cách d (m)', fontsize=12)
axs[1].set_ylabel(r'Tổng năng lượng W ($\mu J$)', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].fill_between(d_arr, W_d, color='red', alpha=0.1)

# --- Đồ thị 3: W theo kappa ---
axs[2].plot(kappa_arr, W_kappa, color='green', linewidth=2.5)
axs[2].set_title(r'$W$ phụ thuộc $\kappa$ ($W \propto \kappa$)', fontsize=14, pad=15)
axs[2].set_xlabel(r'Hằng số điện môi $\kappa$', fontsize=12)
axs[2].set_ylabel(r'Tổng năng lượng W ($\mu J$)', fontsize=12)
axs[2].grid(True, linestyle='--', alpha=0.6)
axs[2].fill_between(kappa_arr, W_kappa, color='green', alpha=0.1)

fig.suptitle('Sự phụ thuộc của năng lượng điện trường (W) vào các tham số', fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
