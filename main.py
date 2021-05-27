import numpy as np
from tkinter import *
import tkinter as tk

def sieve(X, n):
    return np.setdiff1d(X, [n**2 + n*y for y in range(0, X[-1])])



class App(tk.Tk):
    def __init__(self, root):
        self.root = root
        root.title('Sieve of Eratosthenes')
        root.geometry('800x800')
        self.label = Label(root, text="Input Size of List").grid(row=0)
        self.e1 = Entry(root)
        self.e1.grid(row=0, column=1)
        self.label_text = StringVar()
        self.label_text.set('Awaiting size of Sieve...')
        self.result = Label(root, textvariable=self.label_text).grid(row=2)
        self.button = Button(root, text='print sieve', command=self.print_result).grid(row=0, column=2)
        self.quit_button = Button(root, text='exit', command=quit).grid(row=0, column=3)

    def createDisplay(self, container):
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
                print(x)
                self.label_text.set(np.array2string(x,separator=','))


if __name__ == '__main__':
    #N = int(input("Enter the size of List: "))
    root = Tk()
    app = App(root)
    root.mainloop()






