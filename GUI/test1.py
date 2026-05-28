import tkinter as tk

root = tk.Tk()

root.title("Hello World")
root.minsize(200,200)
root.geometry("300x300+50+50")

tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text="-Maya Angelou").pack()

image = tk.PhotoImage(file="./who.png")
tk.Label(root, image=image).pack()

root.mainloop()