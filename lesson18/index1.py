'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('image')
        #self.geometry("300x250")
        self.configure(background='#FB966E')

class MyFrame(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(background='#EFBB24')
        self.img =Image.open("brain.png")
        self.brain =ImageTk.PhotoImage(self.img)
        canvas =tk.Canvas(self,
                          width=256,
                          height=256
                          )
        canvas.create_image(128,128,image=self.brain,anchor=tk.CENTER)
        canvas.pack()
        self.pack(expand=True,fill="both")


def main():    
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()
    
if __name__ == "__main__":
    main()