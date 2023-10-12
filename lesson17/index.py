import dataSource
import tkinter as tk
from tkinter import ttk



def main():
    window = tk.Tk()
    window.title("我的家")
    label = tk.Label(window,text="HELLO",font=('Helvetica', '30'))
    label.pack(padx=100,pady=50)
    window.mainloop()
    

if __name__ == "__main__":
    main()