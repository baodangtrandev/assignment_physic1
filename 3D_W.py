import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ==========================================
# 1. HẰNG SỐ VÀ THAM SỐ CỐ ĐỊNH
# ==========================================
EPS_0 = 8.854e-12
S = 0.04          # Diện tích bản tụ (m^2)

# Tham số cố định cho từng đồ thị
kappa_fixed = 1.0 # Cố định kappa cho đồ thị 1
d_fixed = 0.01    # Cố định khoảng cách 10mm cho đồ thị 2
V_fixed = 500     # Cố định hiệu điện thế 500V cho đồ thị 3

# ==========================================
# 2. KHỞI TẠO LƯỚI DỮ LIỆU
# ==========================================
v_arr = np.linspace(0, 1000, 100)
d_arr = np.linspace(0.01, 0.05, 100)
k_arr = np.linspace(1, 10, 100)

# Lưới cho Đồ thị 1: W(V, d)
V_grid1, D_grid1 = np.meshgrid(v_arr, d_arr)
# Lưới cho Đồ thị 2: W(V, k)
V_grid2, K_grid1 = np.meshgrid(v_arr, k_arr)
# Lưới cho Đồ thị 3: W(d, k)
D_grid2, K_grid2 = np.meshgrid(d_arr, k_arr)

# ==========================================
# 3. TÍNH TOÁN NĂNG LƯỢNG (Đổi ra micro-Joules)
# ==========================================
# Đồ thị 1: W theo V và d
W1_total = 0.5 * (kappa_fixed * EPS_0 * S / D_grid1) * (V_grid1**2)
W1_uJ = W1_total * 1e6

# Đồ thị 2: W theo V và kappa
W2_total = 0.5 * (K_grid1 * EPS_0 * S / d_fixed) * (V_grid2**2)
W2_uJ = W2_total * 1e6

# Đồ thị 3: W theo d và kappa
W3_total = 0.5 * (K_grid2 * EPS_0 * S / D_grid2) * (V_fixed**2)
W3_uJ = W3_total * 1e6

# ==========================================
# 4. VẼ CÁC ĐỒ THỊ TRONG MỘT FIGURE
# ==========================================
fig = plt.figure(figsize=(22, 8))

# --- Đồ thị 1: W(V, d) ---
ax1 = fig.add_subplot(131, projection='3d')
surf1 = ax1.plot_surface(V_grid1, D_grid1, W1_uJ, cmap=cm.viridis,
                         linewidth=0, antialiased=True, alpha=0.9)
ax1.set_title(r'$W$ theo $V$ và $d$ ($W \propto \frac{V^2}{d}$)', fontsize=14, pad=10)
ax1.set_xlabel('Hiệu điện thế V (Volts)', fontsize=11, labelpad=8)
ax1.set_ylabel('Khoảng cách d (m)', fontsize=11, labelpad=8)
ax1.set_zlabel(r'Tổng năng lượng W ($\mu J$)', fontsize=11, labelpad=10)
ax1.tick_params(axis='x', pad=0)
ax1.tick_params(axis='y', pad=0)
ax1.tick_params(axis='z', pad=2)
cbar1 = fig.colorbar(surf1, ax=ax1, shrink=0.6, aspect=15, pad=0.05, orientation='horizontal')
cbar1.set_label(r'Tổng năng lượng ($\mu J$)', labelpad=5)
ax1.view_init(elev=25, azim=-130)

# --- Đồ thị 2: W(V, k) ---
ax2 = fig.add_subplot(132, projection='3d')
surf2 = ax2.plot_surface(V_grid2, K_grid1, W2_uJ, cmap=cm.viridis,
                         linewidth=0, antialiased=True, alpha=0.9)
ax2.set_title(r'$W$ theo $V$ và $\kappa$ ($W \propto \kappa V^2$)', fontsize=14, pad=10)
ax2.set_xlabel('Hiệu điện thế V (Volts)', fontsize=11, labelpad=8)
ax2.set_ylabel(r'Hằng số điện môi $\kappa$', fontsize=11, labelpad=8)
ax2.set_zlabel(r'Tổng năng lượng W ($\mu J$)', fontsize=11, labelpad=10)
ax2.tick_params(axis='x', pad=0)
ax2.tick_params(axis='y', pad=0)
ax2.tick_params(axis='z', pad=2)
cbar2 = fig.colorbar(surf2, ax=ax2, shrink=0.6, aspect=15, pad=0.05, orientation='horizontal')
cbar2.set_label(r'Tổng năng lượng ($\mu J$)', labelpad=5)
ax2.view_init(elev=25, azim=-125)

# --- Đồ thị 3: W(d, k) ---
ax3 = fig.add_subplot(133, projection='3d')
surf3 = ax3.plot_surface(D_grid2, K_grid2, W3_uJ, cmap=cm.viridis,
                         linewidth=0, antialiased=True, alpha=0.9)
ax3.set_title(r'$W$ theo $d$ và $\kappa$ $\left(W \propto \frac{\kappa}{d}\right)$', fontsize=14, pad=10)
ax3.set_xlabel('Khoảng cách d (m)', fontsize=11, labelpad=8)
ax3.set_ylabel(r'Hằng số điện môi $\kappa$', fontsize=11, labelpad=8)
ax3.set_zlabel(r'Tổng năng lượng W ($\mu J$)', fontsize=11, labelpad=10)
ax3.tick_params(axis='x', pad=0)
ax3.tick_params(axis='y', pad=0)
ax3.tick_params(axis='z', pad=2)
cbar3 = fig.colorbar(surf3, ax=ax3, shrink=0.6, aspect=15, pad=0.05, orientation='horizontal')
cbar3.set_label(r'Tổng năng lượng ($\mu J$)', labelpad=5)
ax3.view_init(elev=30, azim=45)

fig.subplots_adjust(left=0.01, right=0.99, bottom=0.05, top=0.9, wspace=0.1)
plt.show()