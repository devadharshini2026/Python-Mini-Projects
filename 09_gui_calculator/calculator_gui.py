import tkinter as tk

def click(button_text):
    """Handle button click and update the entry field."""
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


# Create main window
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Helvetica", 20), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, padx=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Helvetica", 16), width=5, height=2,
                       command=lambda t=text: click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the app
root.mainloop()
