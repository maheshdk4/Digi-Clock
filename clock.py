import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, time)  # update every second

# Create window
root = tk.Tk()
root.title('Digital Clock')

# Create label
label = tk.Label(root, font=('Arial', 600), background='black', foreground='lime')
label.pack(anchor='center')

# Start the clock
time()

# Run the application
root.mainloop()
