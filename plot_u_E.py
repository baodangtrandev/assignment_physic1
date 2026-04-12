import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 1. Khởi tạo các hằng số
epsilon_0 = 8.854e-12
kappa = 1.0  # Giả sử môi trường chân không để quan sát mức nền

# 2. Tạo lưới dữ liệu
# V chạy từ 0 đến 1000V
v = np.linspace(0, 1000, 100)
# d chạy từ 0.01m đến 0.05m (10mm - 50mm)
d = np.linspace(0.01, 0.05, 100)
V, D = np.meshgrid(v, d)

# 3. Tính toán mật độ năng lượng u_E
U_E = 0.5 * kappa * epsilon_0 * (V / D)**2

# 4. Vẽ đồ thị 3D
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Vẽ mặt cong với dải màu 'plasma' để thể hiện sự rực rỡ của năng lượng
surf = ax.plot_surface(V, D, U_E, cmap=cm.plasma,
                       linewidth=0, antialiased=True, alpha=0.9)

# 5. Tinh chỉnh nhãn và tiêu đề
ax.set_title(r'Mật độ năng lượng $u_E$ theo $V$ và $d$ ($u_E \propto V^2/d^2$)', fontsize=16, pad=20)
ax.set_xlabel('Hiệu điện thế V (V)', fontsize=12)
ax.set_ylabel('Khoảng cách d (m)', fontsize=12)
ax.set_zlabel(r'Mật độ năng lượng $u_E$ ($J/m^3$)', fontsize=12)

# Thêm thanh màu (Colorbar)
fig.colorbar(surf, shrink=0.5, aspect=10, label='Mật độ năng lượng (J/m³)')

# Góc nhìn tối ưu để thấy độ cong của Parabol và Hyperbol
ax.view_init(elev=25, azim=-120)

plt.tight_layout()
plt.show()