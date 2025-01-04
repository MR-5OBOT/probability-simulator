import tkinter as tk
from tkinter import ttk

# Create main application window
root = tk.Tk()
root.geometry("400x400")  # Set the window size
root.title("Tabbed Application")  # Set the window title

style = ttk.Style()
# style.configure("TNotebook", background="white")
# style.configure("TNotebook.Tab", background="white", padding=[10, 5])
style.theme_use("clam") 
print(style.theme_names())


# Create a Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=20, pady=20)

# Add a frame for the first tab
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Tab 1")

# Add a frame for the second tab
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Tab 2")

# Configure grid for centering widgets in frame1
# frame1.grid_columnconfigure(0, weight=1)  # Left spacing
# frame1.grid_columnconfigure(1, weight=1)  # Middle content column
# frame1.grid_columnconfigure(2, weight=1)  # Right spacing

# Add widgets to Tab 1 and center them
label1 = ttk.Label(frame1, text="Welcome to Tab 1")
label1.pack(pady=5)

entry_1 = ttk.Entry(frame1)
entry_1.pack(pady=5)

button1 = ttk.Button(frame1, text="Click Me")
button1.pack(pady=5)

# Run the application
root.mainloop()
