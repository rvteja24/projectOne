import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
inputVal  = filedialog.askopenfilename()

print("Thanks for the input :)")