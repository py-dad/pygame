import tkinter as tk

import tkinter.ttk as ttk  # themed widgets 

window = tk.Tk()



greeting = tk.Label(text='Hello, Tkinter',
                    foreground='white',
                    background='black',
                    width=10,
                    height=10)

greeting.pack()

button = tk.Button(
    text='Click me!',
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)

button.pack()









window.mainloop()