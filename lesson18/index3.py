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
        self.configure(background='#B481BB')

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.aligement = tk.StringVar(value='center')
        #self.configure(background='#9B90C2')
        ttk.Radiobutton(self,text="咖哩雞排飯",value='雞排',variable=self.aligement,command=self.choised).grid(column=0,row=0,padx=10)
        ttk.Radiobutton(self,text="咖哩唐揚雞",value='唐揚雞',variable=self.aligement,command=self.choised).grid(column=1,row=0,padx=10)
        ttk.Radiobutton(self,text="咖哩炸豬排",value='炸豬排',variable=self.aligement,command=self.choised).grid(column=2,row=0,padx=10)

        self.pack(expand=1, fill='both',padx=10,pady=10)


def main():    
    window = Window()
    myFrame = MyFrame(window,"今天吃咖喱飯！")
    window.mainloop()

if __name__ == "__main__":
    main()