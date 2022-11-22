from tkinter import Image,Label,Tk,PhotoImage
from PIL import ImageTk, Image
import os

window = Tk()
window.resizable(width=False, height=False)
window.title("qr view")  

scriptdir=os.path.abspath(__file__)
os.chdir(scriptdir.removesuffix('/qrview.py'))
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./qr.png'))

img = ImageTk.PhotoImage(Image.open("qr.png"),master = window)
qr = Label(window, image = img)
qr.pack()
window.mainloop()
