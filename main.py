import numpy as np
from tkinter import *
import tkinter as tk

def sieve(X, n):
    return np.setdiff1d(X, [n**2 + n*y for y in range(0, X[-1])])

class App(tk.Tk):
    cells  = []

    def __init__(self, root):
        self.root = root
        self.frame1 = Frame(root,width=700, height=20)
        self.frame2 = Frame(root,width=700, height=700)
        self.cells = []
        root.title('Sieve of Eratosthenes')
        root.geometry('800x800')
        self.label = Label(self.frame1, text="Input Size of List").pack(side=LEFT)
        self.e1 = Entry(self.frame1)
        self.e1.pack(side=LEFT)
        self.label_text = StringVar()
        self.label_text.set('Awaiting size of Sieve...')
        self.result = Label(self.frame2, textvariable=self.label_text).grid(row=0, column=0)
        self.button = Button(self.frame1, text='print sieve', command=self.print_result).pack(side=LEFT)
        self.quit_button = Button(self.frame1, text='exit', command=quit).pack(side=LEFT)
        self.frame1.pack(padx=1, pady=1)
        self.frame2.pack(padx=10, pady=10)


    def createDisplay(self, sieveList):
        square = int(np.ceil(np.sqrt(len(sieveList))))
        for i in range(square):
            for j in range(square):
                if i+j*square < len(sieveList):
                    cell = Frame(self.frame2, bg='white', highlightbackground="black",
                                highlightcolor="black", highlightthickness=1,
                                width=self.frame2.winfo_screenwidth()/square,
                                height=self.frame2.winfo_screenheight()/square,  padx=3,  pady=3)
                    self.update_cells(cell)
                    Label(cell, text=str(sieveList[i+j*square])).pack(side=LEFT)
                    #print(cell)
                    cell.grid(row=j, column=i)

        self.cells[0].config(bg='black')
        #print(sieveList)
        print(self.cells)
        self.label_text.set("")
        return 0

    def print_result(self):
        print(self.e1.get())
        if self.e1.get() != '':
            n = int(self.e1.get())
            # print(type(N))
            if type(n) is int:
                x = np.linspace(2, n, n - 1, dtype=int)
                for i in x:
                    x = sieve(x, i)
                #print(x)
                self.createDisplay(x)
                #self.label_text.set(np.array2string(x,separator=','))

    def update_cells(self, cell):
        self.cells.append(cell)

if __name__ == '__main__':
    #N = int(input("Enter the size of List: "))
    root = Tk()
    app = App(root)
    root.mainloop()






