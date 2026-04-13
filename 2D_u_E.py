import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. HẰNG SỐ VÀ THAM SỐ CỐ ĐỊNH
# ==========================================
EPS_0 = 8.854e-12

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
# 3. TÍNH TOÁN MẬT ĐỘ NĂNG LƯỢNG (J/m^3)
# ==========================================
# Công thức: u_E = 0.5 * kappa * EPS_0 * (V / d)^2
uE_V = 0.5 * kappa_fixed * EPS_0 * (V_arr / d_fixed)**2
uE_d = 0.5 * kappa_fixed * EPS_0 * (V_fixed / d_arr)**2
uE_kappa = 0.5 * kappa_arr * EPS_0 * (V_fixed / d_fixed)**2

# ==========================================
# 4. VẼ ĐỒ THỊ 2D
# ==========================================
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# --- Đồ thị 1: u_E theo V ---
axs[0].plot(V_arr, uE_V, color='blue', linewidth=2.5)
axs[0].set_title(r'$u_E$ phụ thuộc $V$ ($u_E \propto V^2$)', fontsize=14, pad=15)
axs[0].set_xlabel('Hiệu điện thế V (V)', fontsize=12)
axs[0].set_ylabel(r'Mật độ năng lượng $u_E$ ($J/m^3$)', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].fill_between(V_arr, uE_V, color='blue', alpha=0.1)

# --- Đồ thị 2: u_E theo d ---
axs[1].plot(d_arr, uE_d, color='red', linewidth=2.5)
axs[1].set_title(r'$u_E$ phụ thuộc $d$ ($u_E \propto \frac{1}{d^2}$)', fontsize=14, pad=15)
axs[1].set_xlabel('Khoảng cách d (m)', fontsize=12)
axs[1].set_ylabel(r'Mật độ năng lượng $u_E$ ($J/m^3$)', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].fill_between(d_arr, uE_d, color='red', alpha=0.1)

# --- Đồ thị 3: u_E theo kappa ---
axs[2].plot(kappa_arr, uE_kappa, color='green', linewidth=2.5)
axs[2].set_title(r'$u_E$ phụ thuộc $\kappa$ ($u_E \propto \kappa$)', fontsize=14, pad=15)
axs[2].set_xlabel(r'Hằng số điện môi $\kappa$', fontsize=12)
axs[2].set_ylabel(r'Mật độ năng lượng $u_E$ ($J/m^3$)', fontsize=12)
axs[2].grid(True, linestyle='--', alpha=0.6)
axs[2].fill_between(kappa_arr, uE_kappa, color='green', alpha=0.1)

# Thiết lập tiêu đề tổng và tránh lỗi bị che lấp (cắt chữ)
fig.suptitle('Sự phụ thuộc của mật độ năng lượng điện trường ($u_E$) vào các tham số', 
             fontsize=18, fontweight='bold', y=0.98)

# Chừa lại 7% không gian trống phía trên bằng tham số rect
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
