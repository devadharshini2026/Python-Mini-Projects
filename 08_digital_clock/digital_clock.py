import tkinter as tk
import time


def update_time():
    """Update the clock every second."""
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # refresh every 1000 ms (1 sec)


# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.resizable(False, False)

# Style
label = tk.Label(
    root,
    font=("Helvetica", 48, "bold"),
    fg="cyan",
    bg="black"
)
label.pack(expand=True, fill="both")

# Start clock
update_time()

# Run app
root.mainloop()
