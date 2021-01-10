#library create win
import tkinter as tk
#library create label, button
from tkinter import ttk
#library create message
from tkinter import messagebox

#hàm xử lý: hiện thông báo hello word
def say_hello():
	messagebox.showinfo(title='information',message = 'hello '+ str.get())
#create win
win = tk.Tk()
#create title
win.title('Giao Diện Python')
#create label
label = ttk.Label(win, text='Press the button and see effects')
label.grid(column=0,row=0)
#create button
button = ttk.Button(win, text='Press me',command=say_hello)
button.grid(column=1,row=1)
#create edit box
str = tk.StringVar()
edit_box = ttk.Entry(win, textvariable=str)
edit_box.grid(column=0,row=1)
edit_box.focus()
#run win
win.mainloop()