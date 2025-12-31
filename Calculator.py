# tkinter program
# create main window and 
# add the required widgets 
# run the event loop
################ Simple Calculator program ################
import tkinter as tk
def press(v): #to append the data into entry widget, press is used
    entry.insert(tk.END, v)
def clear():
    entry.delete(0, tk.END)
def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="Black")
root.resizable(False, False)

entry = tk.Entry(root, font=("Segeo UI", 20),
                 bg="#2d2d2d", fg="white",
                 bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
r = 1
c = 0
for b in buttons:
    cmd = calc if b == '=' else lambda x=b: press(x)
    tk.Button(root, text=b, command=cmd,
              font=("Segeo UI", 14), width=5, height=2,
              bg="#ff9500" if b in {'/', '*', '-', '+', '='} else "#3a3a3a",
              fg="white", bd=0).grid(row=r, column=c, padx=6, pady=6)
    c += 1
    if c==4:
        c=0
        r += 1
tk.Button(root, text='C', command=clear,
          font=("Segeo UI", 14), 
          bg="#ff3b30", fg="white", bd=0, width=33, height=2).grid(row=r, column=0, columnspan=4, pady=8) 
root.mainloop()