import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ==========================================
# 1. HẰNG SỐ VÀ GIÁ TRỊ CỐ ĐỊNH
# ==========================================
EPS_0 = 8.854e-12
V_fixed = 500  # Giữ cố định hiệu điện thế V = 500V để khảo sát

# ==========================================
# 2. TẠO LƯỚI DỮ LIỆU (MESHGRID)
# ==========================================
# d chạy từ 0.01m đến 0.05m (10mm đến 50mm)
d_arr = np.linspace(0.01, 0.05, 100)
# kappa chạy từ 1 đến 10
k_arr = np.linspace(1, 10, 100)

D, K = np.meshgrid(d_arr, k_arr)

# ==========================================
# 3. TÍNH TOÁN MẬT ĐỘ NĂNG LƯỢNG u_E
# ==========================================
# Công thức: u_E = 0.5 * k * eps_0 * (V/d)^2
U_E = 0.5 * K * EPS_0 * (V_fixed / D)**2

# ==========================================
# 4. VẼ ĐỒ THỊ 3D SURFACE
# ==========================================
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Vẽ mặt cong với dải màu 'plasma'
surf = ax.plot_surface(D, K, U_E, cmap=cm.plasma,
                       linewidth=0, antialiased=True, alpha=0.9)

# Tinh chỉnh Tiêu đề và Nhãn trục
ax.set_title(r'Mật độ năng lượng $u_E$ theo $d$ và $\kappa$ $\left(u_E \propto \frac{\kappa}{d^2}\right)$', 
             fontsize=16, pad=20)
ax.set_xlabel('Khoảng cách d (m)', fontsize=12)
ax.set_ylabel(r'Hằng số điện môi $\kappa$', fontsize=12)
ax.set_zlabel(r'Mật độ năng lượng $u_E$ ($J/m^3$)', fontsize=12)

# Thêm thanh chú thích màu (Colorbar)
fig.colorbar(surf, shrink=0.5, aspect=10, label='Mật độ năng lượng (J/m³)')

# Xoay góc nhìn (Azimuth & Elevation) 
# Góc này được chọn (azim=45) để nhìn thấy rõ sườn dốc của d và chiều tăng của kappa
ax.view_init(elev=30, azim=45)

plt.tight_layout()

# Bạn có thể bỏ comment dòng dưới để tự động lưu ảnh
# plt.savefig('3D_uE_d_kappa.png', dpi=300, bbox_inches='tight')

plt.show()