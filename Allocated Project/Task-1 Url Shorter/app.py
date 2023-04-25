import pyperclip
import pyshorteners
from tkinter import*
root = Tk()
root.geometry("400x200")
root.title("URL SHORTNER")
root.configure(bg="sky blue")
url = StringVar()
url_address = StringVar()


def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short) 



def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root,text="URL Shortener",font="poppins",width=20).pack(pady=10) 
Entry(root, textvariable=url,width = 28) .pack(pady=5)
Button(root, text="Generate url short",width=15, command=urlshortener). pack(pady=7)
Entry(root, textvariable=url_address,width = 15) . pack( pady=5)
Button(root,text="copy url",bg="white", command= copyurl) . pack(pady=5)
root.mainloop()