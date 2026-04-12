import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ==========================================
# 1. KHAI BÁO CÁC THAM SỐ VẬT LÝ
# ==========================================
EPS_0 = 8.854e-12       # Hằng số điện môi chân không (F/m)
V = 500                 # Hiệu điện thế duy trì không đổi (Volts)
d = 0.01                # Khoảng cách giữa 2 bản tụ (m) -> 10mm
side = 0.2              # Chiều dài cạnh bản tụ vuông (m)

kappa_0 = 1.0           # Hằng số điện môi lý tưởng (chân không)
kappa_d = 5.0           # Hằng số điện môi của vật liệu (ví dụ: thủy tinh)

# Tính toán cường độ điện trường và mật độ năng lượng
# Giả sử tụ được nối liên tục với nguồn nên V = const
E = V / d
w_0 = 0.5 * kappa_0 * EPS_0 * (E**2)  # Mật độ năng lượng chân không
w_d = 0.5 * kappa_d * EPS_0 * (E**2)  # Mật độ năng lượng có điện môi

print(f"--- THÔNG SỐ TÍNH TOÁN ---")
print(f"w (chân không) = {w_0:.6f} J/m³")
print(f"w (điện môi)   = {w_d:.6f} J/m³")

# ==========================================
# 2. VẼ ĐỒ THỊ 3D: w(x,y) KHI CÓ ĐIỆN MÔI
#    (Đã fix lỗi đè chữ trục Z và Colorbar)
# ==========================================
x = np.linspace(-side/2, side/2, 50)
y = np.linspace(-side/2, side/2, 50)
X, Y = np.meshgrid(x, y)

# Tạo mảng giá trị không gian chứa điện môi
W_3d = np.full_like(X, w_d)

fig1 = plt.figure(figsize=(10, 7))

# Dịch khung vẽ 3D sang trái một chút để chừa không gian an toàn cho Colorbar
ax1 = fig1.add_axes([0.05, 0.1, 0.75, 0.8], projection='3d')

# Vẽ mặt cong 3D (màu Oranges)
surf = ax1.plot_surface(X, Y, W_3d, cmap='Oranges', alpha=0.85, edgecolor='none')

ax1.set_title(f'Đồ thị 3D: Phân bố mật độ năng lượng $w(x,y)$\n(Có điện môi $\kappa={kappa_d}$)', fontsize=14, pad=20)

# Căn chỉnh nhãn trục (đẩy ra xa bằng labelpad)
ax1.set_xlabel('Trục X (m)', fontsize=12, labelpad=10)
ax1.set_ylabel('Trục Y (m)', fontsize=12, labelpad=10)
ax1.set_zlabel('Mật độ năng lượng w (J/m³)', fontsize=12, labelpad=12)

# Căn chỉnh các con số (đẩy ra xa trục bằng pad)
ax1.tick_params(axis='x', pad=3)
ax1.tick_params(axis='y', pad=3)
ax1.tick_params(axis='z', pad=8)

# Căn chỉnh trục Z cho phù hợp với tỷ lệ
ax1.set_zlim(0, w_d * 1.5)

# Đẩy thanh Colorbar sang bên phải (bằng pad=0.15) để không đè lên trục Z
cbar = fig1.colorbar(surf, shrink=0.5, aspect=10, pad=0.15)
cbar.set_label('w (J/m³)', labelpad=15)

# ==========================================
# 3. VẼ ĐỒ THỊ 2D: SO SÁNH CÓ VÀ KHÔNG CÓ ĐIỆN MÔI
# ==========================================
z = np.linspace(-0.005, 0.015, 1000)

# Hàm xung vuông cho 2 trường hợp
w_z_0 = np.where((z >= 0) & (z <= d), w_0, 0)
w_z_d = np.where((z >= 0) & (z <= d), w_d, 0)

fig2 = plt.figure(figsize=(10, 6))

# Vẽ đường biểu diễn
plt.plot(z * 1000, w_z_d, 'r-', linewidth=2.5, label=f'Có điện môi ($\kappa={kappa_d}$)')
plt.plot(z * 1000, w_z_0, 'b--', linewidth=2.5, label=f'Chân không ($\kappa=1.0$)')

# Tô màu vùng năng lượng để thấy rõ sự chênh lệch diện tích (Tổng năng lượng)
plt.fill_between(z * 1000, w_z_d, color='red', alpha=0.15)
plt.fill_between(z * 1000, w_z_0, color='blue', alpha=0.15)

# Đánh dấu vị trí 2 bản tụ
plt.axvline(0, color='black', linestyle=':', linewidth=1.5)
plt.axvline(d * 1000, color='black', linestyle=':', linewidth=1.5)

# Chú thích đồ thị
plt.title('Đồ thị 2D: So sánh Mật độ Năng lượng $w(z)$', fontsize=14)
plt.xlabel('Trục tọa độ Z (mm)', fontsize=12)
plt.ylabel('Mật độ năng lượng w (J/m³)', fontsize=12)
plt.xlim(-5, 15)
plt.ylim(0, w_d * 1.2)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=11)

# ==========================================
# 4. HIỂN THỊ KẾT QUẢ
# ==========================================
# CHỈ tự động căn lề cho hình 2D để tránh phá vỡ bố cục 3D
fig2.tight_layout()

plt.show()