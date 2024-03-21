from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from main import run, end, progress

root = Tk()
 
root.title('My App')
frm = ttk.Frame(root, padding=10)
root.geometry("200x200")

icon = PhotoImage(file = "./src/icon.png")
root.iconphoto(False, icon)
value_var = 0
 
progressbar =  ttk.Progressbar(orient="horizontal",variable=value_var,  mode="determinate")
progressbar.pack(fill=X, padx=6, pady=6)
 
label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)

label = Label(text="city")
label.pack()

entrythingy = ttk.Entry()
entrythingy.pack()
contents = tk.StringVar()
contents.set("magnitogorsk")
entrythingy["textvariable"] = contents

def click(): 
  global value_var
  global progressbar
  label["text"] = "searching.."
  value_var = 10
  progressbar['value'] = value_var
  root.update_idletasks()
  run()

  value_var = 50
  progressbar['value'] = value_var
  root.update_idletasks()
  result = end()
  value_var = 100
  progressbar['value'] = value_var
  root.update_idletasks()
  label["text"] = "Done!"
  showinfo(title="Info", message=result)
  
button = ttk.Button(text="search", command=click)
button.pack(anchor="s", padx=[0, 0], pady=[10, 0])
button_close = ttk.Button(text="close", command=root.destroy)
button_close.pack(anchor="s", padx=[0, 0], pady=[10, 0])
root.mainloop()