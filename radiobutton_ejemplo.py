import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

def reset():
    selec.set(None)

selec = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Opcion 1', value='1', variable=selec)
r2 = ttk.Radiobutton(window, text='Opcion 2', value='2', variable=selec)
r3 = ttk.Radiobutton(window, text='Opcion 3', value='3', variable=selec)
reset = tkinter.Button(window, text='RESET',command=reset)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)
reset.grid(column=0, row=4, pady=5, padx=5)

window.mainloop()

if __name__ == '__name__':
    main()
