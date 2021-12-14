import pyshorteners
import pyperclip
from tkinter import *



root=Tk()

root.geometry("400x200")
root.title("url shortener")

root.configure(bg="#80A")
url=StringVar()

url_ad=StringVar()


def urlshortener():
    urlad=url.get()
    url_shor=pyshorteners.Shortener().tinyurl.short(urlad)
    
    url_ad.set(url_shor)
    
def copy_url():
    url_shor=url_ad.get()
    pyperclip.copy(url_shor)
    
    
Label(root,text="My URL SHORTENER",font="poppins").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root,text="Generate Short URL",command=urlshortener).pack(pady=7)
Entry(root,textvariable=url_ad).pack(pady=5)
Button(root,text="Copy URL",command=copy_url).pack(pady=5)

root.mainloop()