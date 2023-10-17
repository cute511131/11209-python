import yfinance as yf
import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# 下载数据
data = yf.download("2330.TW", start="2023-01-01")
data.to_csv('台積電.csv')

# 创建 tkinter 窗口
root = tk.Tk()
root.title("股票数据下载")

# 创建 ttk 页面
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# 创建和布局标签、按钮等 ttk 控件
ttk.Label(frame, text="下载股票数据并保存为 CSV 文件").grid(row=0, columnspan=2, pady=10)

def show_data_and_cleanup():
    # 读取 CSV 数据并显示在 ttk 窗口中
    data = pd.read_csv('台積電.csv')
    text = tk.Text(frame, wrap=tk.WORD)
    text.grid(row=2, columnspan=2, padx=10, pady=10)
    text.insert(tk.END, data.to_string())

    # 删除 CSV 文件
    if os.path.exists('台積電.csv'):
        os.remove('台積電.csv')

ttk.Button(frame, text="显示数据", command=show_data_and_cleanup).grid(row=1, column=0, pady=10)
ttk.Button(frame, text="退出", command=root.quit).grid(row=1, column=1, pady=10)

# 运行 tkinter 主循环
root.mainloop()

