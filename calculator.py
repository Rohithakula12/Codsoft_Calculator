import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons and place them in the grid
row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=evaluate).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main loop
window.mainloop()
