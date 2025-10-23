import tkinter as tk

root = tk.Tk()
root.title("Drawing with Canvas")
root.minsize(300, 200)

# Create the canvas
canvas = tk.Canvas(root, bg="blue", height=500, width=500)
canvas.pack()  # Show the canvas

# Define the rectangle coordinates
rec = 10, 10, 100, 50

# Draw the rectangle
canvas.create_rectangle(rec, fill="green")

#Draw the circle
circle = 200, 50, 300, 100
canvas.create_oval(circle, fill="orange")

# Polygon (triangle here)
canvas.create_polygon(350, 50, 450, 100, 400, 150, fill="yellow", outline="black", width=2)

canvas.create_line(50, 150, 300, 150, fill="black", width=3)

canvas.create_arc(50, 250, 150, 350, start=0, extent=150, fill="orange", outline="black")

canvas.create_arc(50, 250, 150, 350, start=0, extent=150, fill="orange", outline="black")

root.mainloop()
