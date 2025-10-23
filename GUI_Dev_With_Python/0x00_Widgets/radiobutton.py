import tkinter as tk 

root = tk.Tk()
root.title("Radio Button")
root.minsize(300,200)

# tk.Radiobutton(root, text ="Metabrains", value = 1).pack()

for text, value in [("Apple", 1),("Banana",2), ("Grape",3)]:
    tk.Radiobutton(root, text=text, value=value, indicator = 0).pack()


root.mainloop()