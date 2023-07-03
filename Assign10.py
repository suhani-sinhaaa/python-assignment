import tkinter as tk
import webbrowser

def display():
    s = e.get()
    print("Navigating to", s)
    webbrowser.open("https://www.youtube.com/results?search_query=" + s)

obj = tk.Tk(className="interface")

label = tk.Label(obj, text="Search:",bg="grey")
label.grid(row=3, column=2)

e = tk.Entry(obj, font=("Times New Roman", 20), width=30,bg="light blue")
e.grid(row=3, column=4)

b = tk.Button(obj, text="Go", font=("Times New Roman", 12), command=display, bg="PINK")
b.grid(row=4, column=3, columnspan=2)

obj.mainloop()
