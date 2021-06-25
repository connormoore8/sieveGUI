import numpy as np
from tkinter import *
import tkinter as tk


def sieve(X, n):
    return np.setdiff1d(X, [n**2 + n*y for y in range(0, X[-1])])

class App(tk.Tk):
    cells = []
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
    def __init__(self, root):
        self.root = root
        self.frame1 = Frame(root)
        self.frame2 = Frame(root)
        self.cells = []
        root.title('Sieve of Eratosthenes')
        #root.geometry('800x800')
        self.label = Label(self.frame1, text="Input Size of List").pack(side=LEFT)
        self.e1 = Entry(self.frame1)
        self.e1.pack(side=LEFT)
        self.label_text = StringVar()
        self.label_text.set('Awaiting size of Sieve...')
        self.result = Label(self.frame2, textvariable=self.label_text).grid(row=0, column=0)
        self.button1 = Button(self.frame1, text='print cells', command=self.print_result).pack(side=LEFT)
        self.button2 = Button(self.frame1, text='sieve cells', command=self.print_result).pack(side=LEFT)
        self.quit_button = Button(self.frame1, text='exit', command=quit).pack(side=LEFT)
        self.frame1.pack(padx=1, pady=1)
        self.frame2.pack(padx=10, pady=10)


    def createDisplay(self, cellList, sieveList):
        self.cells = []
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        square = 10
        #square = int(np.ceil(np.sqrt(len(cellList))))

        #create a blank cell with '*' symbol
        cell = Frame(self.frame2, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1,
                     # width=self.frame2.winfo_screenwidth()/square,
                     # height=self.frame2.winfo_screenheight()/square,
                     padx=7, pady=7)
        self.update_cells(cell)
        Label(cell, text=str('*'), height=cell.winfo_height(), width=cell.winfo_width()).pack(side=LEFT)
        # print(cell)
        cell.grid(row=0, column=0)
        Grid.columnconfigure(self.frame2, index=1, weight=1)
        Grid.rowconfigure(self.frame2, index=1, weight=1)
        #loop over cells from 2 - > limit
        for i in range(1, len(cellList)+1, 1):
            cell = Frame(self.frame2, bg='white', highlightbackground="black",
                         highlightcolor="black", highlightthickness=1,
                         #width=self.frame2.winfo_screenwidth()/square,
                         #height=self.frame2.winfo_screenheight()/square,
                         padx=7,  pady=7)
            self.update_cells(cell)
            Label(cell, text=str(cellList[i-1][0]), fg=str(cellList[i-1][1]), height=cell.winfo_height(),
                  width=cell.winfo_width()).pack(side=LEFT)
            cell.grid(row=i//10, column=i % 10)
            Grid.columnconfigure(self.frame2, index=i, weight=1)
            Grid.rowconfigure(self.frame2, index=i, weight=1)
        self.cells[0].config(bg='black')
        #print(sieveList)
        #return 0

    def print_result(self):
        print(self.e1.get())
        if self.e1.get() != '':
            n = int(self.e1.get())
            # print(type(N))
            if isinstance(n, int):
                data = list(zip(np.linspace(2, n, n-1, dtype=int),['black' for n in range(2, n+1, 1)]))
                #print(data)
                self.createDisplay(data, data)

    def run_sieve(self, n):
        x = np.linspace(2, n, n - 1, dtype=int)
        for i in x:
            x = sieve(x, i)
        # print(x)
        self.createDisplay(x, x)

    def update_cells(self, cell):
        self.cells.append(cell)

if __name__ == '__main__':
    #N = int(input("Enter the size of List: "))
    root = Tk()
    app = App(root)
    root.mainloop()






