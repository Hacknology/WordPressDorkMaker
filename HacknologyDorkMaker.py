from random_words import RandomWords
import requests
import urllib.request
import google

from tkinter import Tk, Button, Label
from tkinter import StringVar, IntVar
from tkinter import *
def update(new):
    var.set(new)
def kodlar():
    rw = RandomWords()
    o = int(s.get())
    kelime = rw.random_words(count=o)
    wp_dork = ['("Comment on Hello world!")', '("author/admin")', '("uncategorized")', '("Just another WordPress site")', '("/wp/hello-world/")']
    for word in kelime:
        for dork in wp_dork:
            x = dork+word
            f = open("dork.txt", "a+")
            f.write(x + "\n")
            f.close()

    
pencere = Tk()
pencere.geometry("800x600+100+100")
img = PhotoImage(file="arkaplan.gif")
arka = Label(image=img)
arka.pack()
var = StringVar()
var.set("Kelime sayisini girin: ")
baslik = pencere.title("Hacknology THT DorkMaker")
pencere.geometry("300x50+600+460")
pencere.wm_iconbitmap("simge.ico")
pencere.tk_setPalette("black")
etiket = Label(textvariable=var,
               fg="blue",
               bg="#000000",
               font="Helvetica 12 bold")
etiket.pack(side=TOP)
s = Entry()

s.pack()
dugme = Button(text="Basla!",command=kodlar, fg="black", bg="green")

dugme.pack(side=BOTTOM)


mainloop()
        
