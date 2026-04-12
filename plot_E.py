import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 1. Khởi tạo dữ liệu
# V chạy từ 0 đến 1000 (V)
v = np.linspace(0, 1000, 100)
# d chạy từ 0.01 đến 0.05 (m) - tránh d=0 để không bị lỗi chia cho 0
d = np.linspace(0.01, 0.05, 100)

V, D = np.meshgrid(v, d)

# 2. Công thức tính cường độ điện trường E
E = V / D

# 3. Vẽ đồ thị 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Vẽ mặt cong (Surface plot)
surf = ax.plot_surface(V, D, E, cmap=cm.viridis,
                       linewidth=0, antialiased=True, alpha=0.8)

# 4. Tinh chỉnh giao diện
ax.set_title(r'Sự phụ thuộc của $E$ vào $V$ và $d$ ($E = V/d$)', fontsize=15)
ax.set_xlabel('Hiệu điện thế V (Volts)', fontsize=12)
ax.set_ylabel('Khoảng cách d (m)', fontsize=12)
ax.set_zlabel('Cường độ điện trường E (V/m)', fontsize=12)

# Thêm thanh chú thích màu sắc
fig.colorbar(surf, shrink=0.5, aspect=10, label='Độ lớn E (V/m)')

# Điều chỉnh góc nhìn để thấy rõ độ dốc
ax.view_init(elev=30, azim=-135)

plt.tight_layout()
plt.show()