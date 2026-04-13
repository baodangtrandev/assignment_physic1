import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np

# ==============================================================================
# Các Hằng số Vật lý & Thiết lập Toàn cục
# ==============================================================================
EPSILON_0 = 8.854e-12  # Hằng số điện môi của chân không (F/m)
AREA = 0.04            # Diện tích của các bản tụ điện (m^2) [ví dụ: 20cm x 20cm]
A_SZ = np.sqrt(AREA) / 2.0  # Nửa chiều rộng của bản tụ (m)

# Tính toán giá trị Năng lượng Mật độ Trần (Maximum possible u_E)
# dùng để cố định thang màu (colorscale) giúp tiện quan sát sự thay đổi
MAX_V = 1000
MIN_D = 0.001
MAX_KAPPA = 10
MAX_E = MAX_V / MIN_D
MAX_U_E = 0.5 * MAX_KAPPA * EPSILON_0 * (MAX_E ** 2) # Xấp xỉ 44.27 J/m³

# ------------------------------------------------------------------------------
# Khởi tạo Ứng dụng Dash
# ------------------------------------------------------------------------------
app = dash.Dash(__name__)
app.title = "Mô phỏng Năng lượng Tụ điện (3D Vectors)"

app.layout = html.Div(style={'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 'padding': '20px'}, children=[
    html.H2(
        "Tụ điện phẳng- Mô phỏng mật độ năng lượng 3D",
        style={'textAlign': 'center', 'color': '#2C3E50', 'marginBottom': '0px'}
    ),
    html.P(
        "Mô hình 3D bằng ma trận vector (Cones): Mũi tên biểu diễn hướng của điện trường E. "
        "Màu sắc của vector thay đổi động thể hiện độ lớn của mật độ năng lượng",
        style={'textAlign': 'center', 'color': '#7F8C8D', 'marginBottom': '40px'}
    ),
    
    html.Div([
        # --- Bảng Thanh trượt ---
        html.Div([
            html.H4("Bảng điều khiển vật lý", style={'borderBottom': '2px solid #ECF0F1', 'paddingBottom': '10px'}),
            
            html.Label(["Điện áp ", html.B("V"), " (Volts) | Khoảng: 0 - 1000V"]),
            dcc.Slider(
                id='voltage-slider',
                min=0, max=1000, step=10, value=500,
                marks={0: '0', 250: '250', 500: '500', 750: '750', 1000: '1000V'},
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            
            html.Div(style={'height': '40px'}),
            
            html.Label(["Khoảng cách ", html.B("d"), " (m)"]),
            dcc.Slider(
                id='distance-slider',
                min=0.025, max=0.05, step=0.001, value=0.025,
                marks={0.025: '25mm', 0.05: '50mm'},
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            
            html.Div(style={'height': '40px'}),
            
            html.Label(["Hằng số điện môi ", html.B("κ"), " | Khoảng: 1 - 10"]),
            dcc.Slider(
                id='kappa-slider',
                min=1, max=10, step=0.1, value=1.0,
                marks={1: '1', 3: '3', 5: '5', 8: '8', 10: '10'},
                tooltip={"placement": "bottom", "always_visible": True}
            ),

            html.Div(id='output-stats', style={
                'marginTop': '40px',
                'padding': '20px',
                'backgroundColor': '#F8F9F9',
                'borderRadius': '5px',
                'borderLeft': '4px solid #3498DB'
            })
            
        ], style={
            'width': '30%', 
            'display': 'inline-block', 
            'verticalAlign': 'top', 
            'backgroundColor': 'white',
            'padding': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
        }),
        
        # --- Bảng Đồ thị ---
        html.Div([
            dcc.Graph(id='3d-plot', style={'height': '70vh', 'width': '100%'})
        ], style={'width': '65%', 'display': 'inline-block', 'float': 'right'})
    ], style={'maxWidth': '1400px', 'margin': '0 auto'})
])

# ------------------------------------------------------------------------------
# Callback Tính Toán & Vẽ Đồ Thị 3D Vector
# ------------------------------------------------------------------------------
@app.callback(
    [Output('3d-plot', 'figure'),
     Output('output-stats', 'children')],
    [Input('voltage-slider', 'value'),
     Input('distance-slider', 'value'),
     Input('kappa-slider', 'value')]
)
def update_simulation(voltage, distance, kappa):
    # 1. Các Tính toán Vật lý
    E = voltage / distance
    u_E_max = 0.5 * kappa * EPSILON_0 * (E ** 2)
    total_energy = u_E_max * (AREA * distance)
    
    # 2. Xây dựng Đồ thị
    fig = go.Figure()
    
    # Khối hộp biểu diễn Năng lượng u_E bằng màu sắc (Mesh3d Cube)
    # Theo chuẩn hệ trục mới:
    # Trục X: Khoảng cách giữa 2 bản tụ
    # Trục Y: Chiều dài
    # Trục Z: Chiều rộng
    x_box = [0, 0, 0, 0, distance, distance, distance, distance]
    y_box = [-A_SZ, -A_SZ, A_SZ, A_SZ, -A_SZ, -A_SZ, A_SZ, A_SZ]
    z_box = [-A_SZ, A_SZ, A_SZ, -A_SZ, -A_SZ, A_SZ, A_SZ, -A_SZ]
    
    # Chỉ mục tạo các hình tam giác (faces) cho 6 mặt của khối lập phương
    i_box = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
    j_box = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
    k_box = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6]
    
    fig.add_trace(go.Mesh3d(
        x=x_box, y=y_box, z=z_box,
        i=i_box, j=j_box, k=k_box,
        intensity=[u_E_max] * 8, # Ánh xạ màu theo u_E_max cho tất cả 8 đỉnh
        colorscale='Turbo',
        cmin=0, cmax=0.075, # Cố định dải màu trong khoảng 0-0.075 J/m³ để phù hợp với giới hạn mới
        opacity=0.35,       # Giảm độ mờ xuống mức trung bình để hiển thị rõ Vector bên trong
        colorbar=dict(title='Mật độ<br>Năng Lượng (J/m³)', x=0.85),
        name='Khối Năng lượng',
        hovertext=[f'Mật độ (u_E): {u_E_max:.2f} J/m³'] * 8,
        hoverinfo='text'
    ))

    # Độ dày của bản tụ (m)
    t = 0.003
    
    # Vẽ Bản Tụ Trái (ở x=0, dày vào chiều x âm)
    fig.add_trace(go.Mesh3d(
        x=[-t, -t, -t, -t, 0, 0, 0, 0], 
        y=y_box, 
        z=z_box,
        i=i_box, j=j_box, k=k_box,
        color='silver', opacity=0.95, name='Bản cực (0V)'
    ))
    
    # Vẽ Bản Tụ Phải (ở x=distance, dày về chiều x dương)
    fig.add_trace(go.Mesh3d(
        x=[distance, distance, distance, distance, distance+t, distance+t, distance+t, distance+t],
        y=y_box, 
        z=z_box,
        i=i_box, j=j_box, k=k_box,
        color='#E67E22', opacity=0.95, name=f'Bản cực ({voltage}V)'
    ))

    # Vẽ Ma trận Mũi tên (Vector E) chỉ hướng điện trường
    # Hướng từ bản dương sang bản âm dọc theo trục X
    vec_grid = 4
    vx = np.linspace(max(0.005, distance * 0.2), distance * 0.8, 3)
    vy = np.linspace(-A_SZ * 0.6, A_SZ * 0.6, vec_grid)
    vz = np.linspace(-A_SZ * 0.6, A_SZ * 0.6, vec_grid)
    
    VX, VY, VZ = np.meshgrid(vx, vy, vz)
    
    u_dir = -1.0 if voltage > 0 else 1.0
    u_vec = np.ones_like(VX.flatten()) * u_dir
    v_vec = np.zeros_like(VY.flatten())
    w_vec = np.zeros_like(VZ.flatten())
    
    if voltage != 0:
        fig.add_trace(go.Cone(
            x=VX.flatten(), y=VY.flatten(), z=VZ.flatten(),
            u=u_vec, v=v_vec, w=w_vec,
            sizemode='scaled',
            sizeref=0.4, # Tự động thu phóng dựa trên domain để render không bị lỗi
            colorscale='Reds', # Màu đỏ tương phản dễ render WebGL hơn Custom colors
            showscale=False,
            name='Chiều Điện trường E',
            hoverinfo='skip'
        ))
    
    # Tinh chỉnh giao diện và góc nhìn 3D
    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[-0.01, 0.06], title="Trục X: Khoảng cách (m)"),
            yaxis=dict(range=[-0.15, 0.15], title="Trục Y: Chiều dài (m)"),
            zaxis=dict(range=[-0.15, 0.15], title="Trục Z: Chiều rộng (m)"),
            aspectratio=dict(x=0.6, y=1, z=1)
        ),
        margin=dict(l=0, r=0, b=0, t=10),
        legend=dict(yanchor="top", y=0.9, xanchor="left", x=0.1)
    )
    
    stats_html = [
        html.H3("Dữ liệu vật lý"),
        html.P([html.Strong("Cường độ điện trường (E): "), f"{E:,.2f} (V/m)"]),
        html.P([html.Strong("Mật độ năng lượng (u_E): "), f"{u_E_max:,.6f} (J/m³)"]),
        html.P([html.Strong("Tổng năng lượng (W): "), f"{total_energy:,.8f} (J)"])
    ]

    return fig, stats_html

# ==============================================================================
# Điểm bắt đầu Thực thi Mã
# ==============================================================================
if __name__ == '__main__':
    try:
        app.run(debug=True, port=8050)
    except Exception as e:
        app.run(debug=False, port=8051)
