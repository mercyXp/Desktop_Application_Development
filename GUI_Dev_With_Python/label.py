import tkinter as tk

root = tk.Tk()
root.title("Label")

label = tk.Label(root, text = " label in Tkinter is used to display text and images and it is widely used through put the tkinter application and i will advice all developers to use this widget", bg = "lightgreen", font = "calibri", wraplength = 500, padx = 20, pady= 20)

label.pack()

root.mainloop()