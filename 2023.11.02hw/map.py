import tkinter as tk
from PIL import Image, ImageTk
import folium
import os

# 创建主窗口
root = tk.Tk()
root.title("地图标记示例")

# 创建地图
map_location = folium.Map(location=[25.044006, 121.507157], zoom_start=15)
folium.Marker(location=[25.044006, 121.507157], popup="台北市中正区重庆南路一段122号").add_to(map_location)

# 保存地图为图片文件
map_location.save("taipei_map.html")
os.system("wkhtmltoimage taipei_map.html taipei_map.png")

# 打开地图图片
map_image = Image.open("taipei_map.png")
map_photo = ImageTk.PhotoImage(map_image)

# 创建一个Label来显示地图图片
map_label = tk.Label(root, image=map_photo)
map_label.pack()

# 运行主循环
root.mainloop()
