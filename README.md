# Đồ Án / Bài Tập Vật Lý 1: Mô Phỏng Tụ Điện Phẳng

Đây là kho lưu trữ bài tập mô phỏng vật lý liên quan đến tụ điện phẳng. Các chương trình trong dự án này giúp tính toán, vẽ đồ thị tĩnh bằng Matplotlib, và cung cấp một mô hình mô phỏng 3D tương tác trên nền web bằng Dash & Plotly để minh hoạ trực quan.

---

## Hướng dấn cài đặt và chạy code

### 1. Yêu cầu hệ thống
- Môi trường cài đặt Python 3.7+ trở lên.

### 2. Cài đặt các thư viện cần thiết
Mở terminal (giao diện dòng lệnh) tại thư mục chứa mã nguồn (`Assignment`) và chạy lệnh sau để tải về các thư viện phụ thuộc (như `dash`, `plotly`, `numpy`, `matplotlib`):

```bash
pip install -r requirements.txt
```

### 3. Cách chạy các phân đoạn code
Dự án bao gồm 2 nhóm file chính:

* **Mô phỏng 3D tương tác trên Web (Khuyến nghị xem):**
  - **Files:** `capacitor_simulation.py` và `simulation_2-3.py`
  - Đây là các ứng dụng Dashboard, cho phép bạn điều chỉnh bằng thanh trượt các thông số như Hiệu điện thế (V), Khoảng cách (d), Hằng số điện môi ($\kappa$) và xem khối 3D mật độ năng lượng thay đổi.
  - **Cách chạy:**
    ```bash
    python capacitor_simulation.py
    ```
  - **Lưu ý:** Sau khi chạy lệnh này, Terminal sẽ hiển thị một đường link dạng `http://127.0.0.1:8050`. Bạn hãy copy và dán vào trình duyệt web (Chrome, Edge, Safari...) để xem và tương tác với đồ hoạ. Để dừng mô phỏng, nhấn `Ctrl + C` ở terminal.

* **Các file bài toán & phân tích tĩnh (Vẽ đồ thị Matplotlib):**
  - **Files Bài tập:** `2-2.py`, `2-3.py`, `2-4.py` chứa phần giải cho các câu hỏi cụ thể, render ra các đồ thị tĩnh 2D và 3D.
  - **Files Biểu diễn xu hướng:** Các file có tiền tố `plot_*.py` (ví dụ `plot_u_E.py`, `plot_E.py`) dùng để phân tích mối tương quan của các biến số vật lý.
  - **Cách chạy:**
    ```bash
    python 2-2.py
    ```
    *(Tương tự thay tên cho các file khác. Code sẽ vẽ đồ thị và hiện lên trong cửa sổ pop-up. Bạn đóng cửa sổ đó để code thực thi xong).*

---

## Giải thích ý nghĩa các hình ảnh trong folder `export`

Thư mục `export` chứa các hình ảnh tĩnh lưu lại kết quả đầu ra của các kịch bản chạy code giúp minh hoạ cho các báo cáo vật lý. 

**1. Các kết quả theo bài tập cụ thể:**
* `2D_2-2.png` & `2D_2-3.png`: Đồ thị 2D thể hiện mật độ năng lượng (hàm $w(z)$ hoặc $u_E(z)$) phân bố ra sao theo trục Z (phương vuông góc với bản tụ). Năng lượng chỉ tập trung ở giữa hai bản tụ và bằng 0 ở bên ngoài.
* `3D_2-2.png` & `3D_2-3.png`: Đồ thị 3D biểu diễn bề mặt không gian mật độ năng lượng nằm giữa khu vực khe của 2 bản tụ. Do điện trường tụ phẳng là đều nên mặt này tạo thành một mặt phẳng nằm ngang.
* `2-4.png`: Hình ảnh kết quả tương ứng khi chạy nghiệm cho bài toán 2-4.

**2. Hình ảnh mô phỏng Web Dashboard:**
* `simulation_3D_u_E.png`: Hình chụp màn hình khối hộp 3D cho dự án Dash, thể hiện cả véctơ hình nón chỉ điểm hướng dòng điện trường $\vec{E}$ và bề mặt ánh xạ tương ứng màu sắc biểu tượng Mật độ Năng lượng $u_E$.
* `simulation_2D_u_E.png`: Phiên bản rút gọn hoặc mặt cắt đồ thị mô phỏng mật độ thay vì khối 3D toàn diện.

**3. Đồ thị khảo sát sự phụ thuộc vật lý:**
* `E~V-d.png`: Sự biến thiên của **Cường độ điện trường (E)** dưới tác động của Hiệu điện thế (V) và Khoảng cách giữa 2 bản (d).
* `u_E~V-d.png`: Mối tương quan cho thấy **Mật độ năng lượng (u_E)** thay đổi theo hàm của (V) và (d).
* `u_E~k-V.png`: Mật độ năng lượng (u_E) biến động thế nào trên lưới hai trục: Hằng số điện môi ($\kappa$) và Hiệu điện thế (V).
* `u_E~k-d.png`: Mặt cong tương quan giữa Mật độ năng lượng (u_E) với Hằng số điện môi ($\kappa$) và Khoảng cách (d).
