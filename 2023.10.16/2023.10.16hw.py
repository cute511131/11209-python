'''
學習Canvas
'''
import yfinance as yf
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        #self.geometry("300x250")
        #self.configure(background='#E79460')

class GetPassword(Dialog):

    def body(self, master):
        self.title("Enter New Password")

        tk.Label(master, text='Old Password:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='New Password:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='Enter New Password Again:').grid(row=2, sticky=tk.W)

        self.oldpw = tk.Entry(master, width=16, show='*')
        self.newpw1 = tk.Entry(master, width=16, show='*')
        self.newpw2 = tk.Entry(master, width=16, show='*')

        self.oldpw.grid(row=0, column=1, sticky=tk.W)
        self.newpw1.grid(row=1, column=1, sticky=tk.W)
        self.newpw2.grid(row=2, column=1, sticky=tk.W)
        return self.oldpw
    
    def buttonbox(self):
        '''add standard button box.

        override if you do not want the standard buttons
        '''

        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)

        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="日期")
        self.tree.heading('#2', text="開盤")
        self.tree.heading('#3', text="最高")
        self.tree.heading('#4', text="最低")
        self.tree.heading('#5', text="收市")
        self.tree.heading('#6', text="收盤價adj")
        self.tree.heading('#7', text="成交量")


    

        data = yf.download("2303.TW", start="2023-01-01")
        data.to_csv('台積電.csv')

        contacts = []
        for data in range(1,100):
            contacts.append([f'first {data}',f'last {data}',f'email{data}:example.com'])

        for contact in contacts:
            self.tree.insert('',tk.END,value=contact)
        
        self.tree.pack()

        self.tree.bind('<<TreeviewSelect>>',self.item_selected)

       
        
    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        print(item_dict['values'])
        dialog = GetPassword(self)
        
    


def main():    
    window = Window()
    myFrame = MyFrame(window,"股票分析")    
    window.mainloop()

if __name__ == "__main__":
    main()