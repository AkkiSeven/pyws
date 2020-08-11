def hello():
    print('Hello there' )

from tkinter import *
tk = Tk()
btn = Button(tk, text="click me" , command = hello)
btn.pack()
tk.deiconify()
tk.mainloop()

