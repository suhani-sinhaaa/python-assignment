import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Spotify")

l1 = tk.Label(root, text="First Name:", font=("Times New Roman", 28))
l1.grid()
fname = tk.Entry(root, font=("Times New Roman", 30))
fname.grid()

l2 = tk.Label(root, text="Last Name:", font=("Times New Roman", 28))
l2.grid()
Lname = tk.Entry(root, font=("Times New Roman", 28))
Lname.grid()

Cn = tk.Label(root, text="Contact Number:", font=("Times New Roman", 28))
Cn.grid()
Pnum = tk.Entry(root, font=("Times New Roman", 28))
Pnum.grid()

C1 = tk.Label(root, text="The song or podcast that you viewed on social media")
C1.grid()
con = tk.Entry(root, font=("Times New Roman", 28), bg="#8E44AD")
con.grid()

s1 = tk.Label(root, text="The site from where did you come to know about us")
s1.grid()

urls = {
    "Instagram Ads": "https://help.instagram.com/",
    "Facebook Ads": "https://www.facebook.com/help",
    "YouTube Ads": "https://support.google.com/youtube/?hl=en#topic=9257498",
}

def faq():
    webbrowser.open("https://community.spotify.com/t5/FAQs/tkb-p/Spotify-Answers")

def store():
    f = fname.get()
    L = Lname.get()
    p = Pnum.get()
    c = con.get()
    selected_option = option_var.get()
    url = urls[selected_option]

    with open("Database.txt", "a") as file:
        file.write(f"\nFirst Name: {f}\nLast Name: {L}\nContact Number: {p}\nContent: {c}\nSite from which you got to know about us: {selected_option}")

    faq()
    webbrowser.open(url)

option_var = tk.StringVar(root)
option_var.set(list(urls)[0])

options = list(urls.keys())
website_dropdown = tk.OptionMenu(root, option_var, *options)
website_dropdown.config(bg="#8E44AD")
website_dropdown.grid()

T1 = tk.Label(root, text="")
b = tk.Button(root, text="Submit", font=("Times New Roman", 15), command=store)
b.grid(row=14)

tk.mainloop()
