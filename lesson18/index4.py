'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        self.geometry("300x250")
        self.configure(background='#77969A')

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.aligement = tk.StringVar(value='left')
        ttk.Radiobutton(self,text="左邊",value='left',variable=self.aligement,command=self.choised).grid(column=0,row=0,padx=10)
        ttk.Radiobutton(self,text="中間",value='center',variable=self.aligement,command=self.choised).grid(column=1,row=0,padx=10)
        ttk.Radiobutton(self,text="右邊",value='right',variable=self.aligement,command=self.choised).grid(column=2,row=0,padx=10)
        self.pack(expand=1, fill="both",padx=10,pady=10)
        print(self.winfo_class())
        self.style = ttk.Style(self)
        self.style.configure('TLabelframe',font=('Helvetica',20),background='#33A6B8',foreground='#2EA9DF')

    def choised(self):
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")
    s = ttk.Style()
    print(s.theme_names())
    print(s.theme_use())
    window.mainloop()

if __name__ == "__main__":
    main()