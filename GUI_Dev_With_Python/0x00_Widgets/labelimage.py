import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Open the image
image = Image.open("image.jpg")

#resize image
image = image.resize((400, 300))  # width x height

# Convert to a PhotoImage
img = ImageTk.PhotoImage(image)

# Create a label with the image
label = tk.Label(root, image=img)
label.pack()

root.mainloop()
