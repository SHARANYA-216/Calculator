# scientific_calc.py
import tkinter as tk
import math

# --- Helpers ---
def safe_eval(expr: str):
    expr = expr.replace('^', '**')

    # Custom math functions (degree-based)
    allowed = {
        'sin': lambda x: math.sin(math.radians(x)),
        'cos': lambda x: math.cos(math.radians(x)),
        'tan': lambda x: math.tan(math.radians(x)),
        'asin': lambda x: math.degrees(math.asin(x)),
        'acos': lambda x: math.degrees(math.acos(x)),
        'atan': lambda x: math.degrees(math.atan(x)),
        'log': math.log10,     # base-10
        'ln': math.log,        # natural log
        'sqrt': math.sqrt,
        'exp': math.exp,
        'pi': math.pi,
        'e': math.e,
        'abs': abs,
        'round': round
    }

    return eval(expr, {"__builtins__": None}, allowed)

# --- GUI actions ---
def press(v):
    functions = {'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'ln', 'sqrt', 'exp'}
    if v in functions:
        entry.insert(tk.END, v + '(')
    elif v == '%':
        entry.insert(tk.END, '/100')
    elif v == 'pi':
        entry.insert(tk.END, 'pi')
    elif v == 'e':
        entry.insert(tk.END, 'e')
    else:
        entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def backspace():
    s = entry.get()
    if s:
        entry.delete(len(s)-1, tk.END)

def evaluate():
    expr = entry.get()
    try:
        result = safe_eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# --- UI ---
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="black")
root.resizable(False, False)

entry = tk.Entry(
    root, font=("Segoe UI", 20),
    bg="#2d2d2d", fg="white",
    bd=0, justify="right"
)
entry.grid(row=0, column=0, columnspan=5, padx=12, pady=12, ipady=10)

buttons = [
    '7', '8', '9', '/', '⌫',
    '4', '5', '6', '*', '(',
    '1', '2', '3', '-', ')',
    '0', '.', '=', '+', 'C',
    'sin', 'cos', 'tan', 'log', 'ln',
    'sqrt', '^', '%', 'pi', 'e'
]

for i, b in enumerate(buttons):
    row = 1 + (i // 5)
    col = i % 5

    if b == '=':
        cmd, bg = evaluate, "#ff9500"
    elif b == 'C':
        cmd, bg = clear, "#ff3b30"
    elif b == '⌫':
        cmd, bg = backspace, "#8e8e93"
    else:
        cmd, bg = lambda x=b: press(x), "#3a3a3a"

    tk.Button(
        root, text=b, command=cmd,
        font=("Segoe UI", 14),
        width=5, height=2,
        bg=bg, fg="white", bd=0
    ).grid(row=row, column=col, padx=6, pady=6)

# Keyboard support
root.bind('<Return>', lambda e: evaluate())
root.bind('<BackSpace>', lambda e: backspace())
for ch in '0123456789.+-*/()%^':
    root.bind(ch, lambda e, c=ch: press(c))

root.mainloop()
