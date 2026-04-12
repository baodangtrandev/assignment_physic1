import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ==========================================
# 1. HẰNG SỐ VÀ GIÁ TRỊ CỐ ĐỊNH
# ==========================================
EPS_0 = 8.854e-12
d_fixed = 0.01  # Giữ cố định khoảng cách d = 10mm (0.01m) để khảo sát

# ==========================================
# 2. TẠO LƯỚI DỮ LIỆU (MESHGRID)
# ==========================================
# V chạy từ 0 đến 1000V
v_arr = np.linspace(0, 1000, 100)
# kappa chạy từ 1 đến 10
k_arr = np.linspace(1, 10, 100)

V, K = np.meshgrid(v_arr, k_arr)

# ==========================================
# 3. TÍNH TOÁN MẬT ĐỘ NĂNG LƯỢNG u_E
# ==========================================
U_E = 0.5 * K * EPS_0 * (V / d_fixed)**2

# ==========================================
# 4. VẼ ĐỒ THỊ 3D SURFACE
# ==========================================
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Vẽ mặt cong với dải màu 'plasma' (tương đồng với ảnh cũ của bạn)
surf = ax.plot_surface(V, K, U_E, cmap=cm.plasma,
                       linewidth=0, antialiased=True, alpha=0.9)

# Tinh chỉnh Tiêu đề và Nhãn trục
ax.set_title(r'Mật độ năng lượng $u_E$ theo $V$ và $\kappa$ ($u_E \propto \kappa V^2$)', 
             fontsize=16, pad=20)
ax.set_xlabel('Hiệu điện thế V (V)', fontsize=12)
ax.set_ylabel(r'Hằng số điện môi $\kappa$', fontsize=12)
ax.set_zlabel(r'Mật độ năng lượng $u_E$ ($J/m^3$)', fontsize=12)

# Thêm thanh chú thích màu (Colorbar)
fig.colorbar(surf, shrink=0.5, aspect=10, label='Mật độ năng lượng (J/m³)')

# Xoay góc nhìn (Azimuth & Elevation) để thấy rõ cả cạnh thẳng và cạnh cong
ax.view_init(elev=25, azim=-125)

plt.tight_layout()

# Bỏ comment dòng dưới để lưu ảnh tự động
# plt.savefig('3D_uE_V_kappa.png', dpi=300, bbox_inches='tight')

plt.show()