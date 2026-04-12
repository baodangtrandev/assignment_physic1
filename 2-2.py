import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ==========================================
# 1. KHAI BÁO CÁC THAM SỐ VẬT LÝ
# ==========================================
EPS_0 = 8.854e-12       # Hằng số điện môi chân không (F/m)
V = 500                 # Hiệu điện thế (Volts)
d = 0.01                # Khoảng cách giữa 2 bản tụ (10mm)
kappa = 1.0             # Tụ lý tưởng (chân không)
side = 0.2              # Chiều dài cạnh bản tụ vuông (m)

# Tính toán mật độ năng lượng w
E = V / d
w_val = 0.5 * kappa * EPS_0 * (E**2)

print(f"Mật độ năng lượng tính toán: w = {w_val:.6f} J/m³")

# ==========================================
# 2. VẼ ĐỒ THỊ 3D: w(x,y) GIỮA HAI BẢN TỤ
#    (Đã fix triệt để lỗi đè chữ trục Z và Colorbar)
# ==========================================
# Tạo lưới tọa độ x, y trên bề mặt bản tụ
x = np.linspace(-side/2, side/2, 50)
y = np.linspace(-side/2, side/2, 50)
X, Y = np.meshgrid(x, y)

# w(x,y) là hằng số tại mọi điểm (x,y)
W_3d = np.full_like(X, w_val)

fig1 = plt.figure(figsize=(10, 7))

# Dịch khung vẽ 3D sang trái một chút để chừa chỗ cho Colorbar bên phải
# Cú pháp: [left, bottom, width, height]
ax1 = fig1.add_axes([0.05, 0.1, 0.75, 0.8], projection='3d')

# Vẽ mặt phẳng thể hiện sự đồng đều
surf = ax1.plot_surface(X, Y, W_3d, cmap='Blues', alpha=0.8, edgecolor='none')

ax1.set_title('Đồ thị 3D: Phân bố mật độ năng lượng $w(x,y)$\n(Tụ điện phẳng lý tưởng)', fontsize=14, pad=20)

# Căn chỉnh nhãn trục
ax1.set_xlabel('Trục X (m)', fontsize=12, labelpad=10)
ax1.set_ylabel('Trục Y (m)', fontsize=12, labelpad=10)
# Giảm labelpad của trục Z xuống 12 để chữ không bị chìa ra quá xa
ax1.set_zlabel('Mật độ năng lượng w (J/m³)', fontsize=12, labelpad=12)

# Căn chỉnh các con số (đẩy ra xa trục một chút cho thoáng)
ax1.tick_params(axis='x', pad=3)
ax1.tick_params(axis='y', pad=3)
ax1.tick_params(axis='z', pad=8) 

# Cố định trục Z để thấy rõ mặt phẳng không bị sát đáy
ax1.set_zlim(0, w_val * 2) 

# FIX LỖI ĐÈ CHỮ Ở ĐÂY: 
# Thêm tham số pad=0.15 để đẩy thanh Colorbar sang hẳn bên phải
cbar = fig1.colorbar(surf, shrink=0.5, aspect=10, pad=0.15)
cbar.set_label('w (J/m³)', labelpad=15)

# (KHÔNG dùng fig1.tight_layout() ở đây vì đã set vị trí thủ công bằng add_axes)

# ==========================================
# 3. VẼ ĐỒ THỊ 2D: w(z) THEO PHƯƠNG VUÔNG GÓC
# ==========================================
# Lấy dải z rộng hơn khoảng cách d để quan sát không gian bên ngoài tụ
z = np.linspace(-0.005, 0.015, 1000)

# w(z) = w_val nếu z nằm trong [0, d], ngược lại = 0
w_z = np.where((z >= 0) & (z <= d), w_val, 0)

fig2 = plt.figure(figsize=(10, 5))

# Vẽ đường w(z)
plt.plot(z * 1000, w_z, 'b-', linewidth=2.5, label=r'$w(z)$ lý tưởng ($\kappa=1$)')

# Tô màu vùng có năng lượng
plt.fill_between(z * 1000, w_z, color='blue', alpha=0.15)

# Đánh dấu vị trí 2 bản tụ
plt.axvline(0, color='red', linestyle='--', linewidth=1.5, label='Bản tụ dưới (z=0)')
plt.axvline(d * 1000, color='green', linestyle='--', linewidth=1.5, label=f'Bản tụ trên (z={d*1000}mm)')

plt.title('Đồ thị 2D: Mật độ năng lượng $w(z)$ theo phương vuông góc', fontsize=14)
plt.xlabel('Trục tọa độ Z (mm)', fontsize=12)
plt.ylabel('Mật độ năng lượng w (J/m³)', fontsize=12)

# Cố định trục Y để đồ thị đẹp hơn
plt.ylim(0, w_val * 1.5)
plt.xlim(-5, 15)

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper right', fontsize=11)

# Tự động căn lề cho hình 2D
fig2.tight_layout()

# ==========================================
# 4. HIỂN THỊ KẾT QUẢ
# ==========================================
plt.show()