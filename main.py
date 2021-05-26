import numpy as np
from tkinter import *
import tkinter as tk

def sieve(X, n):
    return np.setdiff1d(X,[n**2 + n*y for y in range(0,len(X)//n)])

def print_result(result):
    print(e1.get())
    if e1.get()!='':
        N = int(e1.get())
        #print(type(N))
        if type(N) is int:

            X = np.linspace(2, N, N - 1, dtype=int)
            for x in X:
                X = sieve(X, x)
            print(X)
            result.config(text = str(X))


if __name__ == '__main__':
    #N = int(input("Enter the size of List: "))
    root = Tk()
    root.geometry('400x400')
    root.title('Sieve of Eratosthenes')
    label = Label(root, text="Input Size of List").grid(row=0)
    e1 = Entry(root)
    e1.grid(row=0, column=1)
    result = Label(root, text='Awaiting size of Sieve...')
    button = Button(root, text='print sieve', command=(lambda:print_result(result))).grid(row=1)
    quit_button = Button(root, text='exit', command = quit).grid(row=1, column = 1)
    result.grid(row=2)
    #button.bind()
    root.mainloop()
    #tk.mainloop()






