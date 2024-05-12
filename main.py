import tkinter as tk
from app import Application
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'


root = tk.Tk()
app = Application(master=root)
app.mainloop()
