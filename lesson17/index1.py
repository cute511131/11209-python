import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("鄉鎮人口統計")
        self.configure(background='#66BAB7')

        topFrame = tk.Frame(self,background='#20604F')
        label = ttk.Label(topFrame,text="鄉鎮人口統計",font=('Helvetica', '30'))
        label.pack(padx=50,pady=30)
        topFrame.pack()

        bottomFrame = tk.Frame(self,background='#305A56')
        choices = dataSource.cityNames()
        choicesvar = tk.StringVar(value=choices)
        self.listbox = tk.Listbox(bottomFrame,listvariable=choicesvar,width=13)
        self.listbox.pack(pady=20)
        bottomFrame.pack(expand=True,fill='x')

        self.listbox.bind("<<ListboxSelect>>",self.user_selected)

        resultFrame = tk.Frame(self)
        tk.Label(resultFrame,text="年度:").grid(column=0,row=0,sticky="E",pady=3,padx=3)
        tk.Label(resultFrame,text="地區:").grid(column=0,row=1,sticky="E",pady=3,padx=3)
        tk.Label(resultFrame,text="人口數:").grid(column=0,row=2,sticky="E",pady=3,padx=3)
        tk.Label(resultFrame,text="土地面積:").grid(column=0,row=3,sticky="E",pady=3,padx=3)
        tk.Label(resultFrame,text="人口密度:").grid(column=0,row=4,sticky="E",pady=3,padx=3)
        self.yearVar= tk.StringVar()
        tk.Label(resultFrame,textvariable=self.yearVar).grid(column=1,row=0,sticky="W",pady=3,padx=3)
        self.cityVar= tk.StringVar()
        tk.Label(resultFrame,textvariable=self.cityVar).grid(column=1,row=1,sticky="W",pady=3,padx=3)
        self.populationVar= tk.StringVar()
        tk.Label(resultFrame,textvariable=self.populationVar).grid(column=1,row=2,sticky="W",pady=3,padx=3)
        self.areaVar= tk.StringVar()
        tk.Label(resultFrame,textvariable=self.areaVar).grid(column=1,row=3,sticky="W",pady=3,padx=3)
        self.densityVar= tk.StringVar()
        tk.Label(resultFrame,textvariable=self.densityVar).grid(column=1,row=4,sticky="W",pady=3,padx=3)
        resultFrame.pack()

    def user_selected(self,event):
        selectedIndex=self.listbox.curselection()[0]
        cityName=self.listbox.get(selectedIndex)
        datalist=dataSource.info(cityName)
        self.yearVar.set(datalist[0])
        self.cityVar.set(datalist[1])
        self.populationVar.set(datalist[2])
        self.areaVar.set(datalist[3])
        self.densityVar.set(datalist[4])


def main():
    window = Window()    
    window.mainloop()
    

if __name__ == "__main__":
    main()
    

