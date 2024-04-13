import tkinter as tk

def update_label():
    label.config(text="Hello, Tkinter!")

app = tk.Tk()
app.title("Simple Tkinter GUI")

label = tk.Label(app, text="Press the button...")
label.pack()

button = tk.Button(app, text="Click me!", command=update_label)
button.pack()

app.mainloop()
